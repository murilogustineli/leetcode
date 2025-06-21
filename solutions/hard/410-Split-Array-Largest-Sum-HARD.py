"""
https://leetcode.com/problems/split-array-largest-sum/
"""


def split_array_naive(nums, m):
    if not nums:
        return 0
    elif m == 1:
        return sum(nums)
    else:
        min_result = float('inf')
        for j in range(1, len(nums) + 1):
            left, right = sum(nums[:j]), split_array_naive(nums[j:], m - 1)
            min_result = min(min_result, max(left, right))
        return min_result


def split_array(nums, m):
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        tot, cnt = 0, 1
        for num in nums:
            if tot + num <= mid:
                tot += num
            else:
                tot = num
                cnt += 1
        if cnt > m:
            lo = mid + 1
        else:
            hi = mid
    return hi


def main():
    test_cases = [
        ([7, 2, 5, 10, 8], 2),  # 18
        ([1, 2, 3, 4, 5], 2),  # 9
        ([1, 4, 4], 3),  # 4
        ([1, 2, 3, 4, 5], 1)  # 15
    ]
    for nums, m in test_cases:
        print(split_array_naive(nums, m))
        # print(split_array(nums, m))


if __name__ == '__main__':
    main()
