# python3
"""
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
"""

def find_mismatch(text):
    opening_brackets_stack = []
    for i, bra in enumerate(text):
        if bra in "([{":
            opening_brackets_stack.append([i, bra])

        if bra in ")]}":
            if len(opening_brackets_stack) == 0: 
                return (i+1)
            top = opening_brackets_stack.pop()[1]
            if (top == '(' and bra != ')') or (top == '[' and bra != ']') or (top == '{' and bra != '}'):
                return (i+1)
    
    if len(opening_brackets_stack) == 0:
        return 'Success'
    else:
        return (opening_brackets_stack[-1][0] + 1)


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
