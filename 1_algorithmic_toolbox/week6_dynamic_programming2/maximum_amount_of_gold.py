# Uses python3
import sys
import numpy as np

def optimal_weight(W, n, wg):
    value = np.zeros((W + 1, n + 1))

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            value[w, i] = value[w, i-1]
            if wg[i-1] <= w:
                val = value[w - wg[i-1], i - 1] + wg[i-1]
                if value[w, i] < val:
                    value[w, i] = val
    return int(value[W, n])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, n, w))
