"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/
"""
import numpy as np


def construct2DArray(original, m, n):
    array = []
    if len(original) == m*n:
        for i in range(0, len(original), n):
            array.append(original[i:i+n])
    return array


def construct2DArrayNumPy(original, m, n):
    if len(original) != m*n:
        return []

    array = np.array(original).reshape(m, n)
    return array


def main():
    test_cases = [
        ([1, 2, 3, 4], 2, 2),
        ([1, 2, 3], 1, 3),
        ([1, 2], 1, 1)
    ]
    for array, m, n in test_cases:
        print(construct2DArray(array, m, n))
        # print(construct2DArrayNumPy(array, m, n))


if __name__ == '__main__':
    main()
