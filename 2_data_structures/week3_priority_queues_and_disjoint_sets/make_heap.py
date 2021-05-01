# python3
def left_child(i):
    return 2*i + 1
def right_child(i):
    return 2*i + 2

def sift_down(i, H):
    sz = len(H)
    min_idx = i
    l = left_child(i)
    if l <= (sz-1) and H[l] < H[min_idx]:
        min_idx = l
    r = right_child(i)
    if r <= (sz-1) and H[r] < H[min_idx]:
        min_idx = r
    if i != min_idx:
        H[i], H[min_idx] = H[min_idx], H[i]
        swaps.append([i, min_idx])
        sift_down(min_idx, H)
    return H

def build_heap(data):
    global swaps
    swaps = []
    n = len(data)
    for i in range(n//2 - 1, -1, -1):
         data = sift_down(i, data)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
