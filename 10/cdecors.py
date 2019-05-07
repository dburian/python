#!/usr/bin/env python3
"""
    Class decorator
"""


def log_class(cls):
    def log_access(self, name):
        attr = object.__getattribute__(self, name)
        if name.startswith('_') or not callable(attr):
            return attr
        else:
            def wrapper(*args, **kwargs):
                print(f'Method entry {name}')
                result = attr(*args, **kwargs)
                print(f'Method exit {name}')
                return result
            return wrapper
    cls.__getattribute__ = log_access
    return cls

@log_class
class test_cls:
    def __init__(self, num):
        self.num = num

    def method(self, string):
        print(f'string passed is {string}')
        print(f'num is {self.num}')

    def _private_method(self):
        print('This is from a private method')

    other_method = method

    @staticmethod
    def staticmethod():
        print('This is from a static method')

a = test_cls(7)
a.num
a.method('Blablublublí')
a._private_method()
a.other_method('Blablablaluli')
a.staticmethod()
