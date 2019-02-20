def recursive_fibonacci(n):
    return n - 1 if n == 1 or n == 2 else recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def dynamic_fibonacci(n):
    size = n+2
    memoized = [0] * size
    memoized[2] = 1
    for i in range(3,size):
        memoized[i] = memoized[i-1] + memoized[i-2]
    return memoized[n]

