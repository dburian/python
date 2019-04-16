#!/usr/bin/env python3
'''
   Programm that implements map
'''

from sys import argv
from functools import reduce

def my_map(func, iterable):
    '''
        My map implementation
    '''
    return [func(x) for x in iterable]


def usage():
    '''
        Prints usage of program.
    '''
    print(f'{argv[0]} <lambda> @ <strings separated by spaces>' +
          '--returns elements of list after applying lambda')


if __name__ == '__main__':
    try:
        SEP = argv.index('@')
    except ValueError:
        usage()
        print(argv)
        exit()

    LAMB = eval(reduce( lambda x,y: x + ' ' + y, argv[1:SEP]))
    LIS = argv[SEP+1:]
    print(my_map(LAMB, LIS))

#./my_map.py "lambda x: x[::-1]"  @ ahoj jak se mas nezajdeme si nekam
