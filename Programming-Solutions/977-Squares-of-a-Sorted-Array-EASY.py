"""
https://leetcode.com/problems/squares-of-a-sorted-array/
"""


# Simple way to solve the problem
def sortedSquares(nums):
    nums = [i**2 for i in nums]
    return sorted(nums)


# Another way to solve the problem
def sorted_squares(nums):
    ans = [0] * len(nums)
    l, r = 0, len(nums)-1
    while l <= r:
        low, high = abs(nums[l]), abs(nums[r])
        if low > high:
            ans[r - l] = low * low
            l += 1
        else:
            ans[r - l] = high * high
            r -= 1
    return ans


def main():
    test_cases = [
        [-4, -1, 0, 3, 10],
        [-7, -3, 2, 3, 11],
        [-3, -1, 4, 7, 12]
    ]
    for array in test_cases:
        print(sortedSquares(array))
        print(sorted_squares(array))


if __name__ == '__main__':
    main()
