"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""


def findDuplicates(nums):
    dic = {}
    lst = []
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            lst.append(i)
    return lst


def main():
    test_cases = [
        [4, 3, 2, 7, 8, 2, 3, 1],
        [1, 1, 2],
        [1]
    ]
    for array in test_cases:
        print(findDuplicates(array))


if __name__ == '__main__':
    main()
