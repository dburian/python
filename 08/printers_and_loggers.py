#!/usr/bin/env python3
'''
   Program with Logger, Printer and Formatter
'''

import sys
import abc
from enum import IntEnum


class IPrinter(abc.ABC):

    @abc.abstractmethod
    def set_formatter(self, formatter):
        pass

    @abc.abstractmethod
    def print(self, message):
        print(message)


class IFormatter(abc.ABC):

    @abc.abstractmethod
    def get_style(self, message):
        return message


class LogLevel(IntEnum):
    FINEST = 0
    FINER = 1
    FINE = 2
    INFO = 3
    WARNING = 4
    SEVERE = 5


class Logger:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.level = 0
        self.printers = []

    def set_level(self, level):
        self.level = level

    def add_printer(self, printer):
        self.printers.append(printer)

    def log(self, level, message):
        print("in log")
        if level > self.level:
            for printer in self.printers:
                printer.print(f'[{self.name}] {message}')


class Printer(IPrinter):
    def __init__(self, out):
        super().__init__()
        self.out = out
        self.formatter = None

    def set_formatter(self, formatter):
        self.formatter = formatter

    def print(self, message):
        if self.formatter is None:
            print(message, file=self.out)
        else:
            print(self.formatter.get_style(message), file=self.out)


class Formatter(IFormatter):
    def __init__(self, prefix):
        super().__init__()
        self.prefix = prefix

    def get_style(self, message):
        return self.prefix + ' -- ' + message



def test():
    form = Formatter("In my own words: ")
    prin = Printer(sys.stdout)
    prin.set_formatter(form)

    log = Logger('My log')
    log.set_level(LogLevel.INFO)
    log.add_printer(prin)

    log.log(LogLevel.FINE, "Something unimportant happening")
    log.log(LogLevel.SEVERE, "Fatal morte")


if __name__ == '__main__':
    test()
