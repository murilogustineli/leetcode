"""
https://leetcode.com/problems/spiral-matrix/
"""


def spiralOrder(matrix):
    rows = len(matrix)-1
    cols = len(matrix[0])-1
    spiral = []
    i, j = 0, 0
    bound = [0, rows]
    side = [0, cols]

    # 4 movements: left, down, right, up
    while len(spiral) < (rows+1)*(cols+1):
        # 1. Going right
        while i == side[0] and j <= side[1]:
            spiral.append(matrix[i][j])
            j += 1
        j -= 1
        bound[0] += 1  # update boundary
        # 2. Going down
        while j == side[1] and i < bound[1]:
            i += 1
            spiral.append(matrix[i][j])
        j -= 1
        side[1] -= 1  # update side
        # 3. Going left
        while i == bound[1] and j >= side[0]:
            spiral.append(matrix[i][j])
            j -= 1
        j += 1
        bound[1] -= 1
        # 4. Going up
        while j == side[0] and i > bound[0]:
            i -= 1
            spiral.append(matrix[i][j])
        side[0] += 1
        j += 1

    return spiral[:(rows+1)*(cols+1)]


def spiralOrder_simple(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder_simple([*zip(*matrix)][::-1])


def main():
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ]
    for matrix in test_cases:
        print(spiralOrder(matrix))
        print(spiralOrder_simple(matrix))


if __name__ == '__main__':
    main()
