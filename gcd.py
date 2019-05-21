# 更相减损法求最大公约数
def gcd_minus(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    divisor = 1
    while num1 % 2 == 0 and num2 % 2 == 0:
        num1, num2 = num1 // 2, num2 // 2
        divisor *= 2
    while num1 != num2:
        if num1 < num2:
            num1, num2 = num2, num1
        if num2 > num1 - num2:
            num1, num2 = num2, num1 - num2
        else:
            num1 = num1 - num2
    divisor *= num1
    return divisor


# 辗转相除法求最大公约数
def gcd_divide(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    return num2
