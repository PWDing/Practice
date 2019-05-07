def lcs(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        return 0
    if str1[-1:] == str2[-1:]:
        return lcs(str1[:-1], str2[:-1]) + 1
    else:
        return max(lcs(str1[:-1], str2), lcs(str1, str2[:-1]))


a='abcdeslglwo'
b='bcdweiorp;jf'
lcs(a, b)