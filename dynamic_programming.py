import gcd


# longest common sub string
def lcs(string1, string2):
    longest = 0
    n, m = len(string2), len(string1)
    cells = [[0] * (n+1) for i in range(m+1)]
    for key1, char1 in enumerate(string1, 1):
        for key2, char2 in enumerate(string2, 1):
            if char1 == char2:
                cells[key1][key2] = cells[key1-1][key2-1] + 1
            if cells[key1][key2] > longest:
                longest = cells[key1][key2]
    return longest


# recursive implementation
def lcs_recursive(string1, string2):
    if len(string1) == 0 or len(string2) == 0:
        return 0
    if string1[-1:] == string2[-1:]:
        return lcs(string1[:-1], string2[:-1]) + 1
    else:
        return max(lcs(string1[:-1], string2), lcs(string1, string2[:-1]))


# longest common sub sequence
def lcq(string1, string2):
    n, m = len(string2), len(string1)
    cells = [[0] * (n+1) for i in range(m+1)]
    for key1, char1 in enumerate(string1, 1):
        for key2, char2 in enumerate(string2, 1):
            cells[key1][key2] = max(cells[key1][key2-1], cells[key1-1][key2])
            if char1 == char2:
                cells[key1][key2] = cells[key1-1][key2-1] + 1
    return cells[m][n]


def make_change(change, min_coins):
    cointypes = [1, 5, 10, 21, 25]
    for cents in range(1, (change+1)):
        coin_nums = cents
        for n in [coin for coin in cointypes if coin <= cents]:
            temp = min_coins[cents-n] + 1
            if temp < coin_nums:
                coin_nums = temp
        min_coins[cents] = coin_nums
    return min_coins[change]


def water_jugs(jug1, jug2, aim):
    if aim > max(jug1, jug2):
        return False

    base_jug = gcd.gcd_minus(jug1, jug2)
    if aim % base_jug == 0:
        return True
    else:
        return False


def knapsack(items, capacity):
    """Solve the knapsack problem
    by finding the most valuable subsequence of items
    that doesn't exceed capacity.

    items must be a sequence of pairs (weight, worth),
    where weight is a non-negative integer and worth is a number.

    capacity is a non-negative integer.

    Return the sum of values in the most valuable subsequence.

    >>> items = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
    >>> knapsack(items, 20)
    29

    """
    num = len(items)
    optimal = [[0] * (capacity+1) for i in range(num+1)]
    for cap in range(1, capacity+1):
        for n in range(1, num+1):
            # wt表示该项所需空间，worth表示该项的价值
            wt = items[n-1][0]
            worth = items[n-1][1]
            if wt > cap:
                optimal[n][cap] = optimal[n-1][cap]
            else:
                """这里选择optimal[n-1][cap-wt]而不是optimal[cap-wt][cap-wt]

                实际上，由于每一项只能选择一次，所以当背包容量大于该项所占空间时
                与背包容量恰好等于该项所占空间计算出的最大价值是一样的
                即optimal[n-1][cap-wt] = optimal[cap-wt][cap-wt]

                但是如果选择optimal[cap-wt][cap-wt]时，
                可能遇到下标超出范围的问题.比如背包容量为20时，一定会超出范围
                还可能遇到重复计算某项的问题.比如背包容量为4,实际最大价值为3
                但是若采用后者则会计算出optimal[1][4]=6

                """
                optimal[n][cap] = max(optimal[n-1][cap],
                                      worth + optimal[n-1][cap-wt])
    return optimal[num][capacity]


def med(origin, goal):
    """Minimum Edit Distance

    假定复制操作花费为5，插入和删除操作都为20
    """
    ori_len = len(origin)
    goal_len = len(goal)

    costs = {'copy': 5, 'in': 10, 'del': 20}
    min_distances = [[0]*(goal_len+1) for n in range(ori_len+1)]

    for i in range(ori_len+1):
        for j in range(goal_len+1):
            if i == 0:
                min_distances[i][j] = min_distances[i][j-1] + costs['in']
            elif j == 0:
                min_distances[i][j] = min_distances[i-1][j] + costs['del']
            else:
                if origin[i-1] == goal[j-1]:
                    cost = costs['copy']
                else:
                    cost = costs['in'] + costs['del']

                min_distances[i][j] = min(
                    min_distances[i-1][j] + costs['del'],
                    min_distances[i][j-1] + costs['in'],
                    min_distances[i-1][j-1] + cost)
    return min_distances[ori_len][goal_len]

if __name__ == '__main__':
    # str1 = 'happy'
    # str2 = 'application'
    # str3 = 'note'
    # str4 = 'node'
    # str5 = 'abcd'
    # str6 = 'eacb'
    # print(lcs(str1, str2))
    # print(lcq(str1, str2))
    # print(lcs_recursive(str1, str2))

    # print(make_change(63, [0]*64))

    # items = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
    # print(knapsack(items, 20))

    str1 = 'AGGCTATCACCTGACCTCCAGGCCGATGCCC'
    str2 = 'TAGCTATCACGACCGCGGTCGATTTGCCCGAC'
    print(med(str1, str2))
