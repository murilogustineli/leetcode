"""
https://leetcode.com/problems/sqrtx/
"""


def mySqrt(x: int) -> int:
    for num in range(x+1):
        if num * num == x:
            return num
        elif num*num > x:
            return num-1


# Using binary search to find the sqrt(x)
def binarySqrt(x):
    low = 0
    high = x
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            output = mid - 1
            high = mid - 1
        else:
            output = mid
            low = mid + 1
    return output


def main():
    test_cases = [5, 4, 6, 8, 16, 144, 160, 0, 1, 2, 3]
    for n in test_cases:
        print(mySqrt(n), binarySqrt(n))


if __name__ == '__main__':
    main()