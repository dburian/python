#!/usr/bin/env python3

'''
    Counts number of occurrences in words passed as a argument
'''

import sys


def count_occ(string):
    '''
        COunts number of occurrences of letters in string
    '''
    occurrences = {}
    for letter in string:
        if letter in occurrences.keys():
            occurrences[letter] += 1
        else:
            occurrences[letter] = 1

    return occurrences


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide string to count occurrences.")
    else:
        print(count_occ(sys.argv[1]))
