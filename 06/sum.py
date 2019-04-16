#!/usr/bin/env python3
'''
    Programm to sum arbitrary number of numbers
'''

from functools import reduce
from sys import argv


def my_sum(*args):
    '''
        Function to sum arbitrary number of numbers
    '''
    int_args = map(lambda x: int(x), args)
    return reduce(lambda x, y: x+y, int_args, 0)


def usage():
    '''
        Prints usage of program.
    '''
    print(f'{argv[0]} <numbers separated by spaces> --returns sum of those numbers')


if __name__ == '__main__':
    if len(argv) < 2:
        usage()
    else:
        print(my_sum(*argv[1:]))
