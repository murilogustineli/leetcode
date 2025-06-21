"""
https://leetcode.com/problems/longest-consecutive-sequence/
"""


def longest_consecutive_naive(nums):
    if len(nums) == 0:
        return 0

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


def longest_consecutive(num):
    num = set(num)
    maxLen = 0
    while num:
        n = num.pop()
        i = n+1
        l1, l2 = 0, 0
        while i in num:
            num.remove(i)
            i += 1
            l1 += 1
        i = n-1
        while i in num:
            num.remove(i)
            i -= 1
            l2 += 1
        maxLen = max(maxLen, l1+l2+1)
    return maxLen


def main():
    test_cases = [
        [100, 101, 4, 200, 1, 3, 2],
        [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    ]
    for nums in test_cases:
        print(longest_consecutive_naive(nums))
        print(longest_consecutive(nums))


if __name__ == '__main__':
    main()
