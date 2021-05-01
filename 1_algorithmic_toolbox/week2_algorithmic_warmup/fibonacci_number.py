def calc_fib(n):
    ls = [0,1]
    if n<=1: return n
    while len(ls)-1 != n:
        ls.append(ls[-1]+ls[-2])
    return ls[-1]

n = int(input())
print(calc_fib(n))
