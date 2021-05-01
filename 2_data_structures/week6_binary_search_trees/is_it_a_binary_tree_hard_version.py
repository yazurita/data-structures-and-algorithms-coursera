#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        self.in_order = []
        self.left_dup = False
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, parent):
        if parent == -1:
            return []
        
        self.inOrder(self.left[parent])
        self.in_order.append(self.key[parent])
        if self.left[parent] != -1 and self.key[self.left[parent]] == self.key[parent]:
            self.left_dup = True
        self.inOrder(self.right[parent])
        
        

def main():
    tree = TreeOrders()
    tree.read()
    if tree.n == 0:
        print('CORRECT')
    else:
        tree.inOrder(0)
        in_order = tree.in_order
        if tree.left_dup == False and in_order == sorted(in_order):
            print("CORRECT")
        else:
            print("INCORRECT")

threading.Thread(target=main).start()