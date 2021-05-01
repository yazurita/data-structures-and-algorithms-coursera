# Uses python3
import sys
import numpy as np

def get_change(money):
    coins = [1, 3, 4]
    if money == 0:
        return 0
    min_num_coins = np.zeros(money+1)
    for m in range(1, money+1):
        min_num_coins[m] = (1e3) + 1
        for c in coins:
            if m >= c:
                num_coins = min_num_coins[m - c] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return int(min_num_coins[-1])

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
