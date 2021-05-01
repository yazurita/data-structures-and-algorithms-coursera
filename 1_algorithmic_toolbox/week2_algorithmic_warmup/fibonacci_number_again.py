def calc_fib(n):
    ls = [0,1]
    if n<=1: return n
    while len(ls)-1 != n:
        ls.append(ls[-1]+ls[-2])
    return ls[-1]

def pisano(m):
    if m <= 1: 
        i = m
        return i

    else:
        i = 2
        current = calc_fib(i) % m
        while True:
            i = i + 1
            previous, current = current, calc_fib(i) % m
            if (previous == 0 and current == 1):
                return i-1
    


def huge_fib(n, m):
    return calc_fib(n % pisano(m) ) % m

n, m = map(int, input().split())
print(huge_fib(n,m))
