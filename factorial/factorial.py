def naive_factorial(n):
    res = 1
    while n > 0:
        res *= n
        n -= 1
    return res

def recursive_factorial(n):
    return 1 if n == 0 else n * recursive_factorial(n-1)

def accumulated_factorial(n, accumulator = 1):
    return accumulator if n == 0 else accumulated_factorial(n-1, n * accumulator)

def dynamic_factorial(n):
    size = n + 1
    memoized = [0] * size
    memoized[0] = 1
    for i in range(1, size):
        memoized[i] = i * memoized[i-1]
    return memoized[n]