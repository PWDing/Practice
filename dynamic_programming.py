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


# bag表示背包容量，items是由物品重量和价值组成的字典
# optimal表示最优解
def knapsack(bag, items, optimal):
    for capacity in range(1, bag+1):
        optimal[capacity] = 0
        for w in [for weight in items.keys() if weight <= capacity]:
            if items[w] > optimal[capacity-w]:
                pass

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

    print(make_change(63, [0]*64))
