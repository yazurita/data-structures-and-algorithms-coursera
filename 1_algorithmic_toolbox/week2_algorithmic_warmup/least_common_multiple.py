def gcd(a, b):
    a, b = sorted([a, b], reverse=True)
    while b!=0:
        a, b = b, a%b
        
    else: return a

def lcm(a, b):
    gcd_ = gcd(a, b)
    return int((a*b)/gcd_)

a, b = map(int, input().split())
print(lcm(a, b))
