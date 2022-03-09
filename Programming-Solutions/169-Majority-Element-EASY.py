"""
https://leetcode.com/problems/majority-element/
"""


def majorityElement(nums):
    d = {}
    for elem in range(len(nums)):
        if nums[elem] not in d.keys():
            d[nums[elem]] = 1
        else:
            d[nums[elem]] += 1
    return max(d, key=d.get)


# Using the Boyer Moore algorithm
def majority_element_boyer_moore(nums):
    res, times = 0, 0
    for i in nums:
        if times == 0:
            res = i
        if i == res:
            times += 1
        else:
            times -= 1
    return res


def main():
    test_cases = [
        [3, 2, 3],  # output: 3
        [2, 2, 1, 1, 1, 2, 2],  # output: 2
        [3, 3, 4]  # output: 3
    ]
    for array in test_cases:
        print(majorityElement(array))
        print(majority_element_boyer_moore(array))


if __name__ == '__main__':
    main()
