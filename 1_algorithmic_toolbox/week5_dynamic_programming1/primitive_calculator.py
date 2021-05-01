# Uses python3
import numpy as np

def prim_calc(n):
    seq = [[0, [0]], [0, [1]]]
    if n == 1:
        return seq[-1]

    for m in range(2, n + 1):
        num_op = [] 

        a = [seq[m-1][0] + 1, seq[m-1][1] + [m]]
        num_op.append(a)

        if m % 2 == 0:
            b = [seq[m//2][0] + 1, seq[m//2][1] + [m]]
            num_op.append(b)
            
        if m % 3 == 0:
            c = [seq[m//3][0] + 1, seq[m//3][1] + [m]]
            num_op.append(c)

        seq.append(min(num_op, key = lambda elem: elem[0]))

    return seq[-1]

if __name__ == '__main__':
    n = int(input())
    result = prim_calc(n)
    print(result[0])
    print(result[1])