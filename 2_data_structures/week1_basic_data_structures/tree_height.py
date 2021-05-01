# python3

import sys
import threading

def main():
    def create_tree(n, parents):
        nodes = [[] for i in range(n)]
        
        for i in range(0, n):
            if parents[i] == -1:
                root = i
            else:
                nodes[parents[i]] += [i]
        return nodes, root


    def compute_height(i):
        if len(tree[i]) == 0:
            return 0
        h = []
        for j in tree[i]:
            h.append(compute_height(j))
        return 1 + max(h)

    n = int(input())
    parents = list(map(int, input().split()))
    tree, root = create_tree(n, parents)
    height = compute_height(root)
    print(height+1)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()