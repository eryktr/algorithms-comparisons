import numpy as np
def recursive_fibonacci(n):
    return n  if n == 0 or n == 1 else recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def dynamic_fibonacci(n):
    if n == 0 or n == 1:
        return n
    size = n+1
    memoized = [0] * size
    memoized[1] = 1
    for i in range(2,size):
        memoized[i] = memoized[i-1] + memoized[i-2]
    return memoized[n]

def matrix_fibonacci(n):
    Q = np.array([[1,1],[1,0]])
    cache = {}

    def get_matrix_power(matrix, power):
        if power == 1:
            return matrix
        if power in cache:
            return cache[power]
        tmp = get_matrix_power(matrix, int(power/2))
        result = tmp @ tmp
        cache[power] = result
        return result

    def get_fibonacci_number(n):
        if n == 0 or n == 1:
            return n
        else: 
            powers = [2**power for (power, digit) in enumerate(reversed(bin(n-1)[2:])) if digit == '1']
            matrices = [get_matrix_power(Q, power) for power in powers]

            while len(matrices) > 1:
                M1 = matrices.pop()
                M2 = matrices.pop()
                res = M1 @ M2
                matrices.append(res)
            return matrices[0][0][0]

    return get_fibonacci_number(n)