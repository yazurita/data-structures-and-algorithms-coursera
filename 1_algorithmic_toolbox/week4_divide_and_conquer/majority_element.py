# Uses python3
import sys

def get_majority_element(a, low, high):
    if low == high:
        return a[low]
    
    mid = low + ((high-low)//2)
    right = get_majority_element(a, mid+1, high)
    left = get_majority_element(a, low, mid)

    if right == left:
        return right
    
    else:
        left_count = sum(1 for i in range(low, high+1) if a[i] == left)
        right_count = sum(1 for i in range(low, high+1) if a[i] == right)
        return left if left_count > right_count else right
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    elem = get_majority_element(a, 0, n-1)
    count = a.count(elem)
    if count > n//2: print(1)
    else: print(0)