# T(n)=O(n),S(n)=O(n)
def power2(n):
    if n == 0:
        return 1
    else:
        return power2(n-1) << 1


def sqr(n):
    return n * n


# 2^n=2^(n/2)*2^(n/2)
# T(n)=O(lgn)
def better_power2(n):
    if n == 0:
        return 1
    if n % 2 == 0:
        # 左移一位，相当于n/2一次
        return sqr(better_power2(n >> 1))
    else:
        # 右移一位，相当于n*2一次
        return sqr(better_power2(n >> 1)) << 1


# 先把n转化为二进制形式，n(10)=2^a+2^b+2^c+...(b)
# 则2^n=2^(2^a+2^b+2^c+...)=2^(2^a)*2^(2^b)*2^(2^c)*...
# T(n)=O(lgn),S(n)=O(1)
def bitwise_power2(n):
    # 累积项
    power_n = 1
    # 累乘项
    p = 2
    while n > 0:
        # 只要二进制数位展开中为1的项
        if n & 1:
            power_n *= p

        n >>= 1
        # 这里p=2^(2^k),k=0,1,2,3...
        # 即p=2^1,2^2,2^4,2^8...
        p *= p
    return power_n


# 推广至一般情况
def power(a, n):
    power_ = 1
    p = a
    while n > 0:
        if n & 1:
            power_ *= p

        n >>= 1
        p *= p
    return power_


print(power(4, 3))
