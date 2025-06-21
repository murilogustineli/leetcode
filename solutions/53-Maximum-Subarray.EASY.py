"""
https://leetcode.com/problems/maximum-subarray/
"""


def max_subarray_naive(nums):
    total, max_total = 0, nums[0]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            total = sum(nums[i:j])
            max_total = max(total, max_total)

    return max_total


def max_subarray_fast(nums):
    for i in range(1, len(nums)):
        nums[i] = max(nums[i - 1] + nums[i], nums[i])
    return max(nums)


def main():
    # Test cases
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8]
    ]
    for nums in test_cases:
        print(max_subarray_naive(nums), max_subarray_fast(nums))


if __name__ == '__main__':
    main()
