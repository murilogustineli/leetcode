"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""
import bisect


# Naive approach
def kth_smallest_naive(matrix, k):
    array = sorted([matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[i]))])
    return array[k - 1]


# Binary search
def kth_smallest_binary_search(matrix, k):
    low, high = matrix[0][0], matrix[-1][-1]
    while low < high:
        mid = (low + high) // 2
        if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
            low = mid + 1
        else:
            high = mid
    return low


# Sorting approach
def kth_smallest_sorting(matrix, k):
    array = []
    for row in matrix:
        array += row
    return sorted(array)[k - 1]


def main():
    test_cases = [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8),  # 13
        ([[-5]], 1),  # -5
        ([[1, 2], [1, 3]], 2),  # 1
        ([[1, 2], [1, 3]], 1),  # 1
        ([[1, 2], [1, 3]], 4),  # 3
        ([[1, 2], [3, 3]], 1),  # 1
        ([[1, 2], [1, 3]], 3),  # 2
        ([[1, 2], [1, 3]], 2)  # 1
    ]
    for matrix, k in test_cases:
        print(kth_smallest_naive(matrix, k))
        print(kth_smallest_binary_search(matrix, k))
        print(kth_smallest_sorting(matrix, k))
        print()


if __name__ == '__main__':
    main()
