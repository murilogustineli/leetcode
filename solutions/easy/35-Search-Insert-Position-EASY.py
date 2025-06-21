"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
"""


# Binary Search algorithm
def searchInsert(array, target):
    start, end = 0, len(array)-1

    if array[end] < target:
        return end + 1
    elif array[start] > target:
        return start

    # Iterate over array while start is less than end
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    min_idx, max_idx = min(start, mid, end), max(start, mid, end)
    if array[min_idx] < target < array[max_idx]:
        return min_idx + 1
    else:
        return max_idx


# SIMPLER SOLUTION
def searchInsert2(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


def main():
    array = [1, 3, 5, 6, 9]
    target = [0, 1, 2, 3, 4, 5, 7, 10]

    for t in target:
        print(searchInsert(array, t), searchInsert2(array, t))


if __name__ == '__main__':
    main()
