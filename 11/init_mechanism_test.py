#!/usr/bin/env python3
"""
    __new__ and __init__ mechanisms with base classes and metaclass
"""
class AMeta(type):
    def __new__(cls, name, bases, dct):
        print('AMeta.__new__ called')
        print(f'With name: {name}, bases: {bases}, dct: {dct}')
        return super().__new__(cls, name, bases, dct)

    def __init__(self, name, bases, dct):
        print('AMeta.__init__ called')
        print(f'With name: {name}, bases: {bases}, dct: {dct}')

class Ancestor:
    def __new__(cls):
        print('Ancestor.__new__ called')
        return super().__new__(cls)

    def __init__(self):
        print('Ancestor.__init__ called')


class A(Ancestor, metaclass=AMeta):
    def __new__(cls):
        print('A.__new__ called')
        return super().__new__(cls)

    def __init__(self):
        print('A.__init__ called')

a = A()


# When object is constructed, firstly
#   the metaclass __new__ is called
#   on the newly created object metaclass's __init__ is called
#   then class's __new__ is called
#   and then class's __init__ is called
#   -- depends on the implementation of A.__new__ and A.__init__ if Ancestor's methods are called
#   (default implementation calls them)

#The metaclass's __new__ is called with fixed arguments
#and so is metaclass's __init__

#The distinction is, that metaclasses create classes in their __new__ methods, meanwhile 
#classes create instances in their __new__ methods... Thats why type.__new__ has 4 args and 
#object.__new__ has only one. Same name, same methods, different purpose.
