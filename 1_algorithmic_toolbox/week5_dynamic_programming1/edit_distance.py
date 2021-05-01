import numpy as np

# Uses python3
def edit_distance(s, t):
    n = len(s) + 1
    m = len(t) + 1
    d = np.empty((n, m))
    d[:,0] = np.arange(n)
    d[0,:] = np.arange(m)

    for j in range(1, m):
        for i in range(1, n):
            ins = d[i, j-1] + 1
            dele = d[i-1, j] + 1
            match = d[i-1, j-1]
            mismatch = d[i-1, j-1] + 1
            
            if s[i - 1] == t[j - 1]:
                d[i, j] = min(ins, dele, match)
            else:
                d[i, j] = min(ins, dele, mismatch)
    
    return int(d[n-1, m-1])

if __name__ == "__main__":
    print(edit_distance(input(), input()))
