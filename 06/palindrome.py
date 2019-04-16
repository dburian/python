#!/usr/bin/env python3
'''
    Programm to check if argument is a palindrome.
'''

from sys import argv


def check_palindrome(word):
    '''
        Checks if word is palindrome.
    '''
    i = 0
    while i < len(word)//2 and word[i] == word[-1*(i+1)]:
        i += 1

    return i == len(word)//2


def usage():
    '''
        Prints usage of program.
    '''
    print(f'{argv[0]} <word>--returns true if word is palindrome')



if __name__ == '__main__':
    if len(argv) != 2:
        usage()
    else:
        print(check_palindrome(argv[1]))
