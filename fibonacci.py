def iterable(n):
    n, next = 0, 1
    for i in range(1, n):
        n, next = next, n + next
    return n


def divide_recursion(n):
    if n <= 2:
        return n-1
    else:
        return divide_recursion(n-1) + divide_recursion(n-2)


def linear_recursion(n, prev={}):
    if n <= 2:
        return n-1
    try:
        return prev[n]
    except KeyError:
        prev[n] = linear_recursion(n-1, prev) + linear_recursion(n-2, prev)
        return prev[n]


print(iterable(64))
print(linear_recursion(64))
print(divide_recursion(5))
