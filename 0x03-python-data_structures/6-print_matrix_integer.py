#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        row_len = len(row)
        for value in row:
            i += 1
            print("{:d}".format(value), end='')
            if i != row_len:
                print(" ", end='')
        print("")
