#!/usr/bin/env python3
'''
    Programm to sum arbitrary number of numbers
'''

from sys import argv


def fib_gen():
    '''
        Lazy generator for fibonacci numbers
    '''
    yield 0
    yield 1
    lastlast = 0
    last = 1
    while True:
        new = lastlast + last
        lastlast = last
        last = new
        yield new


def fib_nth(nth):
    '''
        Gets the nth fibonacci number
    '''
    i = 0
    for fib in fib_gen():
        if i == nth:
            return fib
        i += 1


def fib_seq_gen(length):
    '''
        Gets the fibbonacci sequence with given length
    '''
    i = 0
    fibs = []
    for fib in fib_gen():
        fibs.append(fib)
        i += 1
        if i == length:
            break

    return fibs


def usage():
    '''
        Prints usage of program.
    '''
    print(f'{argv[0]} <number> --returns fibonacci sequence with given length')


if __name__ == '__main__':
    if len(argv) != 2:
        usage()
    else:
        print(fib_seq_gen(int(argv[1])))
