#!/usr/bin/env python3
"""
    Python shell with extensions
"""

import abc
import sys


class Cmd(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def print_help(self):
        pass

    @abc.abstractmethod
    def exec(self, shell, *args):
        pass


class Help(Cmd):
    @property
    def name(self):
        return 'help'

    def print_help(self):
        print('Write "help" to print out usage of the program')

    def exec(self, shell, *args):
        if len(args) > 0:
            for cmd in args:
                index = shell.find_cmd(cmd)
                if index == -1:
                    print(f'Command {cmd} not found')
                    continue
                else:
                    print(f'Help for {cmd}:')
                    shell.cmds[index].print_help()
                    print()
            return

        print('Write command name to execute that command')
        print('Write "help" followed by command name to print out usage of that command')
        print('Available commands:')
        print([cmd.name for cmd in shell.cmds])


class Exit(Cmd):
    @property
    def name(self):
        return 'exit'

    def print_help(self):
        print('Exits the program')

    def exec(self, shell, *args):
        sys.exit()


class OpenFile(Cmd):
    @property
    def name(self):
        return 'fopen'

    def print_help(self):
        print('Opens a file')

    def exec(self, shell, *args):
        for _file in args:
            try:
                with open(_file) as _f_in:
                    print(f'Opening {_file}:')
                    print(_f_in.read())
            except IOError:
                print(f'File {_file} could not be opened')


class Shell:
    def __init__(self, *args):
        super().__init__()
        self.cmd_list = [Help(), Exit()] + list(args)

    @property
    def cmds(self):
        return self.cmd_list
    
    def find_cmd(self, cmd_name):
        """
            Returns index of command with name cmd_name from cmds. 
            -1 if command name was not found
        """
        try:
            return [cmd.name for cmd in self.cmds].index(cmd_name)
        except ValueError:
            return -1

    def start(self):
        print('Interactive shell start. Write "help" to get help.')
        while True:
            inp = input('>')
            in_words = inp.split(' ')
            cmd_in = self.find_cmd(in_words[0])
            if cmd_in == -1:
                print(f'Command {in_words[0]} was not found.')
                continue

            self.cmds[cmd_in].exec(self, *in_words[1:])


if __name__ == '__main__':
    Shell(OpenFile()).start()
