"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


def findDisappearedNumbers(nums):
    setNum = set(nums)
    arr = []
    for i in range(1, len(nums)+1):
        if i not in setNum:
            arr.append(i)
    return arr


def main():
    test_cases = [
        [4, 3, 2, 7, 8, 2, 3, 1],
        [1, 1]
    ]
    for test in test_cases:
        print(findDisappearedNumbers(test))


if __name__ == '__main__':
    main()
