#!/usr/bin/env python3
'''
   Rectangle class definition
'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def __eq__(self, other):
        return self.width == other.width and \
               self.height == other.height

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


if __name__ == '__main__':
   rec_1 = Rectangle(3,4)
   rec_2 = Rectangle(4,5)

   print(rec_1 == rec_2)
   print(rec_1 < rec_2)
   print(rec_1 >= rec_2)
