"""
https://leetcode.com/problems/range-sum-query-immutable/
"""


class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sumNums = 0
        for i in range(left, right + 1):
            sumNums += self.nums[i]
        return sumNums
        return sum(self.nums[i:j+1])


def main():
    test_cases = [
        [[-2, 0, 3, -5, 2, -1], [0, 2], [2, 5], [0, 5]],
        [[1, 2, 3, 4, 5, 6, 7], [0, 3], [3, 6], [1, 5]]
    ]
    for nums in test_cases:
        numArray = NumArray(nums[0])
        print(numArray.nums)
        print(numArray.sumRange(left=nums[1][0], right=nums[1][1]))
        print(numArray.sumRange(left=nums[2][0], right=nums[2][1]))
        print(numArray.sumRange(left=nums[3][0], right=nums[3][1]))


if __name__ == '__main__':
    main()

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
#
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0,2], [2,5], [0,5]]
