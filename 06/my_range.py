#!/usr/bin/env python3
'''
    Programm to sum arbitrary number of numbers
'''

from sys import argv


def usage():
    '''
        Prints usage of program.
    '''
    print(f'{argv[0]} <arguments for range>--returns list of that range')


def my_range(fst_arg, scd_arg=None, thrd_arg=None):
    '''
        Same behavior as range.
    '''
    def my_inner_range(start, stop, step):
        '''
            Same behavior as range
        '''
        i = start
        continue_cond = (lambda i, stop: i > stop) if step < 0 else (lambda i, stop: i < stop)
        while continue_cond(i, stop):
            yield i
            i += step

    if scd_arg is None:
        return my_inner_range(0, fst_arg, 1)

    if thrd_arg is None:
        return my_inner_range(fst_arg, scd_arg, 1)

    return my_inner_range(fst_arg, scd_arg, thrd_arg)


if __name__ == '__main__':
    if len(argv) > 4:
        usage()
    else:
        int_args = map(lambda x: int(x), argv[1:])
        print(list(my_range(*int_args)))
