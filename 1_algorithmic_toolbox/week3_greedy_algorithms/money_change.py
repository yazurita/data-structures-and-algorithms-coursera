def n_coins(q):
    n = 0
    for i in [10, 5, 1]:
        if q >= i:
            n += int(q / i)
            q = q % i
        else: continue

    return n

q = int(input())
print(n_coins(q))