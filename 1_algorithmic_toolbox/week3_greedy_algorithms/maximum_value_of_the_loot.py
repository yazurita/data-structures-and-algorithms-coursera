# Uses python3
import sys

def get_optimal_value(capacity, w, v):
    value = 0.
    for i in range(n):
        if capacity == 0: 
            return value

        a = min(capacity, w[i])
        value += a*(v[i]/w[i])
        capacity -= a
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    t = tuple(zip(values,weights))
    t_s = sorted(t, key = lambda elem: elem[0]/elem[1], reverse = True )
    v, w = zip(*t_s)
    opt_value = get_optimal_value(capacity, w, v)
    print("{:.10f}".format(opt_value))