"""
https://leetcode.com/problems/concatenation-of-array/
"""


def getConcatenation(nums: list[int]) -> list[int]:
    return nums + nums


def main():
    test_cases = [
        [1, 2, 1],
        [1, 3, 2, 1],
        [2, 4, 6, 7, 7]
    ]
    for array in test_cases:
        print(getConcatenation(array))


if __name__ == '__main__':
    main()
    