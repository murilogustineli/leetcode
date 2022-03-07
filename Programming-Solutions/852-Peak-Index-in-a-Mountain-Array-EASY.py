"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""


def peakIndexInMountainArray_Naive(arr):
    return arr.index(max(arr))


def peakIndexInMountainArray(arr):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid-1] < arr[mid] > arr[mid+1] and mid <= len(arr)-1:
            return mid
        elif arr[mid] < arr[mid+1]:
            low = mid + 1
        else:
            high = mid - 1


def main():
    test_cases = [
        [0, 1, 0],
        [0, 2, 1, 0],
        [0, 1, 2, 3, 1, 0]
    ]
    for array in test_cases:
        # print(peakIndexInMountainArray_Naive(array))
        print(peakIndexInMountainArray(array))


if __name__ == '__main__':
    main()
