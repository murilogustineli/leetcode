"""
https://leetcode.com/problems/two-sum/
"""


def twoSum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]

        if remaining in seen:
            return [seen[remaining], i]

        seen[value] = i


def main():
    test_cases = [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]

    for i in test_cases:
        print(twoSum(i[0], i[1]))


if __name__ == "__main__":
    main()
