"""
https://leetcode.com/problems/contains-duplicate/
"""


def containsDuplicates(nums):
    numSet = set(nums)
    if len(nums) == len(numSet):
        return False
    return True


def main():
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]
    for test in test_cases:
        print(containsDuplicates(test))


if __name__ == '__main__':
    main()
