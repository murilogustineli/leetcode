"""
https://leetcode.com/problems/missing-number/
"""


def missingNumber(nums):
    n = list(range(len(nums)+1))
    for i in range(len(n)):
        if n[i] not in nums:
            return n[i]


# One liner
def missingNumber2(nums):
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)


def main():
    test_cases = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
        [1]
    ]
    for test in test_cases:
        print(missingNumber(test))
        # print(missingNumber2(test))


if __name__ == '__main__':
    main()
