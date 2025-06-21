"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


def removeDuplicates(nums):
    # k is slow pointer
    k = 0
    for n in nums:
        if n != nums[k]:
            # increment slow pointer once
            k += 1
            nums[k] = n

    return k + 1


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
