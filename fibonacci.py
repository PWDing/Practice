def fib_iterable(n):
    fib_n, fib_next = 0, 1
    for i in range(1, n):
        fib_n, fib_next = fib_next, fib_n + fib_next
    return fib_n


def fib_divide_recursion(n):
    if n <= 2:
        return n-1
    else:
        return fib_divide_recursion(n-1) + fib_divide_recursion(n-2)


def fib_linear_recursion(n, prev={}):
    if n <= 2:
        return n-1
    try:
        return prev[n]
    except KeyError:
        prev[n] = fib_linear_recursion(n - 1, prev) + fib_linear_recursion(n - 2, prev)
        return prev[n]


print(fib_iterable(64))
print(fib_linear_recursion(64))
print(fib_divide_recursion(5))
