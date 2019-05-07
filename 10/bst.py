#!/usr/bin/env python3
"""
    Binary Search Tree
"""

from enum import Enum
from sys import argv
from copy import deepcopy

class BST:
    class ItState(Enum):
        Left = -1
        Right = 1
    class NodeIterator:
        def __init__(self, root):
            super().__init__()
            self.root = root
            self.state = BST.ItState.Left

        def __iter__(self):
            return self

        def __next__(self):
            def go_left():
                if self.root.left is None:
                    return go_center()

                while self.root.left is not None:
                    self.root = self.root.left

                self.state = BST.ItState.Right
                return self.root

            def go_center():
                self.state = BST.ItState.Right
                return self.root

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

                
            if self.state == BST.ItState.Left:
                return go_left()

            if self.state == BST.ItState.Right:
                return go_right()

    class ValueIterator:
        def __init__(self, root):
            super().__init__()
            self.it = BST.NodeIterator(root)

        def __iter__(self):
            return self
        
        def __next__(self):
            return self.it.__next__().value

    def __init__(self, value = None, parent = None):
        super().__init__()
        self.left = None
        self.value = value
        self.right = None
        self.parent = parent
        self._size = 1 if self.value is not None else 0

    def insert(self, value):
        def find_empty_pos(self, value):
            """
                Finds position where value should be
                Returns (node, -1|0|1) where the number marks if the searched position
                is left child | node itself | right child
            """
            root = self
            while root.value != value:
                if root.value > value:
                    if root.left is None:
                        return (root, -1)
                    else:
                        root = root.left
                else:
                    if root.right is None:
                        return (root, 1)
                    else:
                        root = root.right
            return (root, 0)

        if self.value is None:
            self.value = value
            self._size += 1
            return True

        (node, num) = find_empty_pos(self, value)
        if num < 0:
            node.left = BST(value, node)
            self._size += 1
            return True
        
        if num > 0:
            node.right = BST(value, node)
            self._size += 1
            return True

        return False

    def to_string(self, spaces): 
        return f'--- Value: {self.value}\n' + \
               spaces * ' ' + f' |-{"" if self.right is None else self.right.to_string(spaces+3)}\n' + \
               spaces * ' ' + f' |-{"" if self.left is None else self.left.to_string(spaces+3)}'

    def __str__(self):
        return f'--- Value: {self.value}\n' + \
               f' |-{"" if self.right is None else self.right.to_string(3)}\n' + \
               f' |-{"" if self.left is None else self.left.to_string(3)} \n'

    def __iter__(self):
        return BST.ValueIterator(self)

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
        
    def __len__(self):
        return self._size

    def __getitem__(self, key):
        if not isinstance(key, int): 
            raise ValueError
        if key >= len(self):
            return BST()
        
        pos = 0
        for node in BST.NodeIterator(self):
            if pos == key:
                return node
            pos += 1

    def __setitem__(self, key, value):
        node = self.__getitem__(key)
        parent = node.parent
        if parent is None:
            node.value = key.value
            node.right = key.right
            node.left = key.left
            # node.parent is left to be None
        else:
            value.parent = parent
            if parent.left is None or parent.left.value != node.value:
                parent.right = value
            else:
                parent.left = value

    def __delitem__(self, key):
        nodeToDel = self.__getitem__(key)

        if nodeToDel.parent is not None:
            if nodeToDel.parent.left is None or nodeToDel.value != nodeToDel.parent.left.value:
                nodeToDel.parent.right = None
            else:
                nodeToDel.parent.left = None
        nodeToDel.parent = None

    def __bool__(self):
        return self.value is not None

def test():
    tree = BST(5)
    print(len(tree))
    print(tree)
    print()
    
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    print(f'After inserting 1,2,3:\n{tree}')
    print()

    print('Iterator:', end=' ')
    for i in tree:
        print(i,end=' ')
    print()

    tree = tree + 7
    print(f'After add operation with 7:\n{tree}')
    print()

    tree += BST(1) + BST(4) + BST(99)
    print(f'After add operations with following trees:')
    print(BST(1))
    print(BST(4))
    print(BST(99))
    print(f'The result is:\n{tree}')
    print()

    print(f'The second item in tree is:\n {tree[2]}')
    print()

    tree[2] = BST(81)
    print(f'After assigning \n{BST(81)} \n to second item in tree: \n{tree}')

    del tree[2]
    print(f'After deleting the second item: \n{tree}')

    print(f'Is there a twenty-first item? {bool(tree[21])}')

if __name__ == '__main__':
    if len(argv) < 2:
        test()
    else:
        with open(argv[1]) as _in:
            tree = BST()
            for num in _in.readline().split(' '):
                tree.insert(int(num))

            print(tree)

