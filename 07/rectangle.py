#!/usr/bin/env python3
'''
   Rectangle class definition 
'''

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        print(self.width * self.height)

    def set_size(self, width, height):
        self.width = width
        self.height = height
