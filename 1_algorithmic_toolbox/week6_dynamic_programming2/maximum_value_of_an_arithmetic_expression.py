# Uses python3
import numpy as np

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    def min_and_max(i, j):
        min_ = 1e5
        max_ = - 1e5
        for k in range(i, j):
            a = evalt(M[i, k], M[k+1, j], op[k])
            b = evalt(M[i, k], m[k+1, j], op[k])
            c = evalt(m[i, k], M[k+1, j], op[k])
            d = evalt(m[i, k], m[k+1, j], op[k])
            min_ = min(min_, a, b, c, d)
            max_ = max(max_, a, b, c, d)
        return [min_, max_]
    
    nums = list(dataset[::2])
    op = list(dataset[1::2])

    n = len(nums)
    m = np.zeros((n, n))
    M = np.zeros((n, n))

    np.fill_diagonal(m, nums)
    np.fill_diagonal(M, nums)

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            m[i, j], M[i, j] = min_and_max(i, j)

    return int(M[0, n-1])


if __name__ == "__main__":
    print(get_maximum_value(input()))
