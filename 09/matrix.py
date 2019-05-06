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

        return Matrix(new_rows)

    def int_product(self, num):
        return Matrix([[num * cell for cell in row] for row in self.get_rows()])

    def int_sum(self, num):
        return Matrix([[num + cell for cell in row] for row in self.get_rows()])

    def __mul__(self, other):
        if isinstance(other, Matrix):
            return self.product(other)
        else:
            return self.int_product(other)

    def __rmul__(self, other):
        return self.int_product(other)

    def __radd__(self, other):
        return self.int_sum(other)

    def __add__(self, other):
        if isinstance(other, Matrix):
            return self.sum(other)
        else:
            return self.int_sum(other)

    def __str__(self):
        _str = ""
        for row in self.get_rows():
            _str += str(row) + '\n'

        return _str

    def __eq__(self, other):
        equal = True
        row_s = self.get_rows()
        row_o = other.get_rows()
    
        for i in range(len(row_s)):
            for j in range(len(row_s[i])):
                equal &= row_s[i][j] == row_o[i][j]

        return equal


if __name__ == '__main__':
    m_id = Matrix([[1,0,0],[0,1,0],[0,0,1]])
    m_test = Matrix([[1,2,3],[4,5,6],[7,8,9]])

    print(m_id * m_test)
    print(m_test * m_id)

    print(m_id + 2)
    print(2 + m_id)

    print(m_id *5)
    print(5*m_id)

    print(m_id == m_id)
    print(m_id != m_test)
