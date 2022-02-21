"""
https://leetcode.com/problems/remove-element/
"""


def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(removeElement(nums, val))
