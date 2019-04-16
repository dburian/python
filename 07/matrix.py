#!/usr/bin/env python3
'''
   Matrix class definition
'''

from functools import reduce


class Matrix:
    def __init__(self, rows):
        super().__init__()
        self.rows = rows

    def append_row(self, row):
        self.rows.append(row)

    def append_column(self, column):
        self.rows = [row.append(number) for (row, number) in zip(self.rows, column)]

    def get_rows(self):
        return self.rows

    def get_columns(self):
        for i in range(0, len(self.rows[0])):
            yield list(map(lambda x: x[i], self.rows))

    def sum(self, other_matrix):
        new_rows = []
        for (row1, row2) in zip(self.rows, other_matrix.get_rows()):
            new_rows.append([row1[i] + row2[i] for i in range(0, len(row1))])

        return Matrix(new_rows)

    def product(self, other_matrix):
        new_rows = []
        def vector_product(vec1, vec2):
            return reduce(lambda x, y: x + y, [vec1[i] * vec2[i] for i in range(0, len(vec1))])

        for row in self.rows:
            new_rows.append([vector_product(row, col) for col in other_matrix.get_columns()])

        return new_rows
