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


str1 = 'happy'
str2 = 'application'
str3 = 'note'
str4 = 'node'
str5 = 'abcd'
str6 = 'eacb'
print(lcs(str1, str2))
print(lcq(str1, str2))
print(lcs_recursive(str1, str2))
