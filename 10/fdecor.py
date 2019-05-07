#!/usr/bin/env python3
"""
    Function decorators
"""

def ignore_errors(function):
    def inner_(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            return None
    return inner_

@ignore_errors
def div(nom, denom):
    return nom / denom


print(div(5, 4))
print(div(5, 0))

def ignore_errors_ext(value):
    def ignore_errors(function):
        def inner_(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except Exception:
                return value
        return inner_
    return ignore_errors


@ignore_errors_ext(0)
def div_ext(nom, denom):
    return nom / denom


print(div_ext(5, 4))
print(div_ext(5, 0))
