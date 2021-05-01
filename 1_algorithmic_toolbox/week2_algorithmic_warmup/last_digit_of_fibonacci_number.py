def last_digit_fib(n):
    ls = [0,1]
    if n<=1: return n
    while len(ls)-1 != n:
        ls.append((ls[-1] + ls[-2])%10)
    return ls[-1]

n = int(input())
print(last_digit_fib(n))
