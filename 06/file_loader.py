#!/usr/bin/env python3
'''
    Programm to sum arbitrary number of numbers
'''

from sys import argv


def usage():
    '''
        Prints usage of program.
    '''
    print(f'{argv[0]} <files separated by space>')
    print('\tpress Enter to display the next line')
    print('\tpress n + Enter to forget the rest of the current file and start' +
          'with the next file')
    print('\tpress q + Enter to terminate the program')
    print('\tor anything else + Enter to display the next line')


def file_loader(files):
    '''
        Returns loader for given files
    '''
    for fil in files:
        print(f'Printing from {fil}')
        yield line_loader(fil)


def line_loader(fil):
    '''
        Returns lines for given file
    '''
    with open(fil) as inp:
        for line in inp:
            yield line[:-1]


def main(files):
    '''
        Main interactive loop of the program
    '''
    for fil in file_loader(files):
        for line in fil:
            print(line)

            inp = input('action :')
            if inp == 'n':
                break
            if inp == 'q':
                exit()


if __name__ == '__main__':
    if len(argv) < 2:
        usage()
    else:
        main(argv[1:])
