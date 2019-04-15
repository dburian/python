#!/usr/bin/env python3

'''
    Calculates result of expression passed as a argument in prefix notation
'''

import sys


def calc(expr):
    '''
        Calculates result of an expression in 'expr' in prefix notation
    '''
    stack = []
    for i in expr:
        if i in "+-*/":
            right = stack.pop()
            left = stack.pop()
            stack.append(str(eval(left + i + right)))
        else:
            stack.append(i)

    if len(stack) > 1:
        print("Expression in invalid form")
        exit(0)

    return stack.pop()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide an expression to be computed")
    else:
        print(calc(sys.argv[1:]))
