"""
https://leetcode.com/problems/plus-one/
"""


def plusOne(digits: list[int]) -> list[int]:
    string = ''
    for i in digits:
        string += str(i)

    string = str(int(string) + int('1'))

    return [int(i) for i in str(string)]


def plusOneComprehension(digits):
    # Converting integers to strings
    string = [str(i) for i in digits]
    # Adding 1 to the total number
    add = str(int(''.join(string)) + 1)
    # Return list of integers
    return [int(i) for i in add]


def main():
    test_cases = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9]
    ]
    for nums in test_cases:
        print(plusOne(nums))
        print(plusOneComprehension(nums))


if __name__ == '__main__':
    main()
