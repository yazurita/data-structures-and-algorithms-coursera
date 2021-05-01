# python3
import sys


def compute_min_refills(distance, tank, stops):
    num_refills = 0
    curr_refill = 0
    x = [0] + stops + [distance]
    n = len(x)

    while curr_refill < (n-1):
        last_refill = curr_refill
        while (curr_refill < (n-1) and x[curr_refill+1] - x[last_refill] <= tank):
            curr_refill += 1
        if curr_refill == last_refill:
            return -1
        if curr_refill < (n-1):
            num_refills += 1
    
    return num_refills


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    stops.sort()
    print(compute_min_refills(d, m, stops))
