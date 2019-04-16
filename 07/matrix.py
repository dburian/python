#!/usr/bin/env python3
'''
   Matrix class definition 
'''


class Matrix:
    def __init__(self, rows):
        super()__init__()
        self.rows = rows

    def append_row(self, row):
        self.rows.append(row)
    
    def append_column(self, column):
        self.rows = [ row.append(number) for (row, number) in zip(self.rows, column)]
    
    def get_rows(self):
        return self.rows

    def sum(self, other_matrix):
        return Matrix([])
