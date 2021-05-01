import sys

def merge(b, c):
    d = []
    global pairs
    if isinstance(b, int): b = [b]
    if isinstance(c, int): c = [c]
    while len(b) != 0 and len(c) != 0:
        if b[0] <= c[0]:
            d.append(b.pop(0))
        else:
            d.append(c.pop(0))
            pairs += 1*len(b)
    d = d + b + c
    return d

def merge_sort(a):
    n = len(a)
    if n == 1:
        return a
    m = n//2
    b = merge_sort(a[0 : m])
    c = merge_sort(a[m :])
    d = merge(b, c)
    return d

if __name__ == '__main__':
    pairs = 0
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    merge_sort(a)
    print(pairs)
