# python3
from random import randint
import numpy as np

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PrecomputedHashes(T, P_sz, p, x):
    T_sz = len(T)
    H = np.empty(T_sz - P_sz + 1)
    S = T[T_sz - P_sz : T_sz]
    H[T_sz - P_sz] = PolyHash(S, p, x)
    y = 1
    for i in range(1, P_sz + 1):
        y = (y * x) % p
    for i in range(T_sz - P_sz - 1, -1, -1):
        H[i] = (x * H[i+1] + ord(T[i]) - y * ord(T[i + P_sz])) % p
    return H

def PolyHash(S, p, x):
    hash_ = 0
    for i in range(len(S) - 1, -1, -1):
        hash_ = (hash_ * x + ord(S[i])) % p
    return hash_

def get_occurrences(P, T):
    p = 10000019
    x = randint(1, p - 1)
    result = []
    pHash = PolyHash(P, p, x)
    H = PrecomputedHashes(T, len(P), p, x)
    for i in range(0, len(T)-len(P)+1):
        if pHash != H[i]:
            continue
        if T[i : i + len(P)] == P:
            result.append(i)
    return result

    

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

