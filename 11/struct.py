#!/usr/bin/env python3
"""
    Definition of struct in python
"""

class MetaStruct(type):
    def __new__(cls, name, bases, namespace):
        org_x = namespace.pop('x') if 'x' in namespace.keys() else None
        org_y = namespace.pop('y') if 'y' in namespace.keys() else None

        namespace['__slots__'] = 'x', 'y'
        namespace['org_x'] = org_x
        namespace['org_y'] = org_y
        
        def struct_init(self, *, x = None, y = None):
            cls = type(self)
            self.x = x if x is not None else cls.org_x
            self.y = y if y is not None else cls.org_y

        def struct_repr(self):
            _str = 'Point('
            if self.x != type(self).org_x:
                _str += f'x={self.x}'
            if self.y != type(self).org_y:
                if self.x != type(self).org_x:
                    _str += ', '
                _str += f'y={self.y}'
            _str += ')'
            return _str

        namespace['__init__'] = struct_init
        namespace['__repr__'] = struct_repr

        _cls = super().__new__(cls, name, bases, namespace)
        return _cls


class Struct(metaclass=MetaStruct):
    pass

class Point(Struct):
    x = 3.5

p = Point(y = 8)
print(p)

p.y = 2
p.x = 3
print(p)

#Uncomment the following line to get an exception
#p.z = None
