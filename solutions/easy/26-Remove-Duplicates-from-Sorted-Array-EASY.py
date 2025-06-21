"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


def removeDuplicates(nums):
    l = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l  # length of the array with unique elements is returned


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
