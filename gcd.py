# 未完成版
def cn_detraction(a, b):
    p = 1
    t = abs(a-b)
    while t != 0:
        if a % 2 == 0 and b % 2 == 0:
            a /= 2
            b /= 2
        else:
            while t % 2 == 0:
                t /= 2
            if a >= b:
                a = t
            else:
                b = t
            t = abs(a - b)
    return int(a * p)


print(cn_detraction(18, 256))
