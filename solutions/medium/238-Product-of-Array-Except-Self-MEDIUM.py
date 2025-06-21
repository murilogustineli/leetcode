"""
https://leetcode.com/problems/product-of-array-except-self/
"""


# Naive function
def product_except_self_naive(nums):
    ans = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod = prod*nums[j]
        ans.append(prod)
    return ans


# 2*O(n) runtime
def productExceptSelf(nums):
    ans = [1] * len(nums)
    pre = 1
    for i in range(len(nums)):
        ans[i] = pre
        pre *= nums[i]
    post = 1
    for j in range(len(nums)-1, -1, -1):
        ans[j] *= post
        post *= nums[j]
    return ans


# O(n) runtime
def productExceptSelf_fast(nums):
    ans = [1] * len(nums)
    pre = 1
    post = 1
    for i in range(len(nums)):
        ans[i] *= pre
        pre *= nums[i]
        ans[~i] *= post
        post *= nums[~i]
    return ans


def main():
    test_cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
        [0, 0],
        [2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ]
    for array in test_cases:
        # print(product_except_self_naive(array))
        print(productExceptSelf(array))
        print(productExceptSelf_fast(array))


if __name__ == '__main__':
    main()
