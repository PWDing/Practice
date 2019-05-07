# 统计整数n的二进制展开中数位1的总数
# 时间复杂度为lgn(log以2为底的n)
def count_ones(num):
    count = 0
    while num > 0:
        # 将num的二进制展开中各个数位和1作位与运算
        if num & 1:
            count += 1
        # 每次将num的二进制展开式向右移一位，相当于原数每次除以2
        num >>= 1
    return count


# 时间复杂度为n的二进制展开中数位为1的线性级数
# 最坏情况为lgn(n的二进制位宽)
def better_count_ones(num):
    count = 0
    while num > 0:
        # 至少有一个1
        count += 1
        # 消除num的二进制展开中中最右边的1
        # 比如num=20，二进制展开为00010100,19=00010011
        # 第一次消除后，num变成16=00010000,15=00001111
        # 第二次消除后，num变成0，循环结束
        num &= num - 1
    return count