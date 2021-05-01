def gcd(a, b):
    a, b = sorted([a, b], reverse=True)
    while b!=0:
        a, b = b, a%b
        

    else: return a

a, b = map(int, input().split())
print(gcd(a, b))