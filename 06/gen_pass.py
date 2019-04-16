#!/usr/bin/env python3
'''
    Program for creating random passwords
'''

from sys import argv
import random as rand
from functools import reduce

def pass_gen(length, num_of_special):
    '''
        Generates password with given length and with given number of special characters
    '''
    passw = []
    for i in range(0, length - num_of_special):
        abc_choice = rand.randint(0, 2)
        if abc_choice == 0:
            passw.append(chr(rand.randint(48, 57)))
        elif abc_choice == 1:
            passw.append(chr(rand.randint(65, 90)))
        else:
            passw.append(chr(rand.randint(97, 122)))

    special = '-_$#@<>;:|/\\(){}[]=+-*.?!'
    for i in range(0, num_of_special):
        rand_spec = rand.choice(special)
        rand_pos = rand.randint(0, len(passw))
        passw.insert(rand_pos, rand_spec)

    return reduce(lambda a, b: a + b, passw, '')


def usage():
    '''
        Prints usage of program.
    '''
    print(f'{argv[0]} <length of password> <number of special character>' +
          '--returns randomly generated password')


if __name__ == '__main__':
    if len(argv) != 3:
        usage()
    else:
        print(pass_gen(int(argv[1]), int(argv[2])))
