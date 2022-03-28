"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/
"""


def findRotation(matrix, target):
    n = len(matrix[0])
    for _ in range(4):
        if matrix == target:
            return True
        else:
            for i in range(len(matrix)):
                for j in range(n):
                    matrix[i].append(matrix[-j - 1].pop(0))
    return False


def main():
    test_cases = [
        ([[0, 1], [1, 0]], [[1, 0], [0, 1]]),
        ([[0, 1], [1, 1]], [[1, 0], [0, 1]]),
        ([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]])
    ]
    for matrix, target in test_cases:
        print(findRotation(matrix, target))


if __name__ == '__main__':
    main()
