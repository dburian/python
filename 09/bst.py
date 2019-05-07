#!/usr/bin/env python3
"""
    Binary Search Tree
"""

from enum import Enum
from sys import argv
from copy import deepcopy

class BST:
    class Iterator:
        class ItState(Enum):
            Left = -1
            Right = 1

        def __init__(self, root):
            super().__init__()
            self.root = root
            self.state = self.ItState.Left

        def __iter__(self):
            return self

        def __next__(self):
            def go_left():
                if self.root.left is None:
                    return go_center()

                while self.root.left is not None:
                    self.root = self.root.left

                self.state = self.ItState.Right
                return self.root.value

            def go_center():
                self.state = self.ItState.Right
                return self.root.value

            def go_right():
                if self.root.right is not None:
                    self.root = self.root.right
                else:
                    return go_up()
                return go_left()

            def go_up():
                if self.root.parent is None:
                    raise StopIteration

                val = self.root.value
                self.root = self.root.parent
                if self.root.left is not None and val == self.root.left.value:
                    return go_center()
                else:
                    return go_up()

                
            if self.state == self.ItState.Left:
                return go_left()

            if self.state == self.ItState.Right:
                return go_right()
                    

    def __init__(self, value = None, parent = None):
        super().__init__()
        self.left = None
        self.value = value
        self.right = None
        self.parent = parent

    def insert(self, value):
        if self.value is None:
            self.value = value
            return True

        root = self
        while root.value != value:
            if root.value > value:
                if root.left is None:
                    root.left = BST(value, root)
                else:
                    root = root.left
            else:
                if root.right is None:
                    root.right = BST(value, root)
                else:
                    root = root.right

        return root.value != value

    def to_string(self, spaces): 
        return f'--- Value: {self.value}\n' + \
               spaces * ' ' + f' |-{"" if self.right is None else self.right.to_string(spaces+3)}\n' + \
               spaces * ' ' + f' |-{"" if self.left is None else self.left.to_string(spaces+3)}'

    def __str__(self):
        return f'--- Value: {self.value}\n' + \
               f' |-{"" if self.right is None else self.right.to_string(3)}\n' + \
               f' |-{"" if self.left is None else self.left.to_string(3)} \n'

    def __iter__(self):
        return BST.Iterator(self)

    def __add__(self, other):
        new = deepcopy(self)

        if isinstance(other, BST):
            for node in other:
                new.insert(node)
        else:
            new.insert(other)
        
        return new

    def __radd__(self, other):
        new = deepcopy()

        new.insert(other)
        return new

    def __iadd__(self, other):
        if isinstance(other, BST):
            for node in other:
                self.insert(node)
        else:
            self.insert(other)
        return self
        
    
def test():
    tree = BST(5)
    print(tree)
    tree.insert(2)
    print(tree)
    tree.insert(3)
    print(tree)


    for i in tree:
        print(i,end=' ')
    print()
    tree + 7

    print(tree)

    tree = tree + 7

    print(tree)

    tree += BST(1) + BST(4) + BST(99)

    print(tree)

if __name__ == '__main__':
    if len(argv) < 2:
        test()
    else:
        with open(argv[1]) as _in:
            tree = BST()
            for num in _in.readline().split(' '):
                tree.insert(int(num))

            print(tree)

