"""
https://leetcode.com/problems/set-matrix-zeroes/
"""
import numpy as np


def setZeros_NumPy(matrix):
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                # matrix[i] = [0]*len(matrix[i])
                row.append(i)
                col.append(j)
    mat = np.array(matrix)
    for i in col:
        mat[:, i] = 0
    for i in row:
        mat[i] = 0
    return mat


def setZeroes(matrix):
    row, col = [], []
    # Iterate over array and identify rows and columns with zeros
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.append(i)
                col.append(j)
    # Modify entire rows and columns in matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j in col:
                matrix[i][j] = 0
            if i in row:
                matrix[i] = [0] * len(matrix[i])

    return matrix


def main():
    test_cases = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    ]
    for matrix in test_cases:
        print(setZeros_NumPy(matrix))
        print(setZeros(matrix))


if __name__ == '__main__':
    main()
