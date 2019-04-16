#!/usr/bin/env python3
'''
   Program with Logger, Printer and Formatter
'''

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
        if level > self.level:
            for printer in self.printers:
                printer.print(f'[{self.name}] {message}')


class Printer:
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


class Formatter:
    def __init__(self, prefix):
        super().__init__()
        self.prefix = prefix

    def get_style(self, message):
        return self.prefix + '--' + message
