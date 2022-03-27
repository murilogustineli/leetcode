"""
https://leetcode.com/problems/rotate-image/
"""


def rotate_naive(matrix):
    ans = []
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            temp.append(matrix[-j-1][i])
        ans.append(temp)
    return ans


# Rotate the matrix in-place
def rotate(matrix):
    length = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(length):
            matrix[i].append(matrix[-j-1].pop(0))
    return matrix


# One-liner solution
def rotate_simple(matrix):
    return list(zip(*matrix[::-1]))


def main():
    test_cases = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # [[7,4,1],[8,5,2],[9,6,3]]
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ]
    for matrix in test_cases:
        # print(rotate_naive(matrix))
        print(rotate(matrix))


if __name__ == '__main__':
    main()
