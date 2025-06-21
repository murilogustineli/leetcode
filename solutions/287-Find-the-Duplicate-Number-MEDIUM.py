"""
https://leetcode.com/problems/find-the-duplicate-number/
"""


def findDuplicate(nums):
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            return i


def main():
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [2, 4, 6, 7, 7]
    ]
    for array in test_cases:
        print(findDuplicate(array))


if __name__ == '__main__':
    main()
