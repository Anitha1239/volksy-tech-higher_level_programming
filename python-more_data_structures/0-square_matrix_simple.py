#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst = []
    for i in matrix:
        sub_matrix = map(lambda num: num**2, i)
        lst.append(list(sub_matrix))
    return lst
