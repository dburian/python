#!/usr/bin/env python3
'''
    Sorts list of numbers passed as an argument
'''

from sys import argv


def select_sort(arr):
    '''
        Sorts array using select sort.
    '''
    for i in range(len(arr)):
        j = pos_of_min(arr[i:])
        arr[i], arr[i+j] = arr[i+j], arr[i]

    return arr


def pos_of_min(arr):
    '''
        Finds the position of a minimal element.
    '''

    min_val = 9e99
    min_pos = -1
    for i in range(len(arr)):
        if arr[i] < min_val:
            min_val, min_pos = arr[i], i

    return min_pos


if __name__ == '__main__':
    if len(argv) < 2:
        print('Provide list to be sorted.')
        exit(-1)

    print(select_sort(list(map(int, argv[1:]))))
