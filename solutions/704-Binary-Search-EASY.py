"""
https://leetcode.com/problems/binary-search/
"""


def search(nums, target):
    low, high = 0, len(nums)-1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    test_cases = [
        [[-1, 0, 3, 5, 9, 12], 9],
        [[-1, 0, 3, 5, 9, 12], 2],
        [[-1, 0, 3, 5, 9, 12], 13]
    ]
    for nums, target in test_cases:
        print(search(nums, target))


if __name__ == '__main__':
    main()
