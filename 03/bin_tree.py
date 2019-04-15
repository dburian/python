#!/usr/bin/env python3

'''
    Prints binary tree with n levels, where n is given as a argument.
'''

import sys


def get_fork(depth):
    '''
        Returns list[element = line] of strings
        of a two-way fork with entered depth
    '''
    fork = []
    for i in range(1, depth+1):
        spaces_out = depth - i
        spaces_in = 1+2*(i-2)
        if spaces_in < 0:
            fork.append(' ' * spaces_out + '*' + ' ' * spaces_out)
        else:
            fork.append(' ' * spaces_out +
                        '*' + ' ' * spaces_in +
                        '*' + ' ' * spaces_out)
    return fork


def get_tree(n_levels):
    '''
        Returns list[element = line] of strings with binary tree of n levels.
    '''
    if n_levels == 1:
        return get_fork(2)

    dos = 2**(n_levels - 1)     # depth of subtree
    return [dos * ' ' + x + ' ' * dos for x in get_fork(dos)] +\
           [x + ' ' + x for x in get_tree(n_levels-1)]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Provide a number.')
    else:
        for line in get_tree(int(sys.argv[1])):
            print(line)
