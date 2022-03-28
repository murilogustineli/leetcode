"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""


def longestConsecutive(nums):
    nums = sorted(set(nums))
    seq, temp = [], [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            temp.append(nums[i])
        else:
            seq.append(temp)
            temp = [nums[i]]

    seq.append(temp)
    return max([len(i) for i in seq])


def main():
    test_cases = [
        [100, 101, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    ]
    for nums in test_cases:
        print(longestConsecutive(nums))


if __name__ == '__main__':
    main()