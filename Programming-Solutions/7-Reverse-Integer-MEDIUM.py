"""
https://leetcode.com/problems/reverse-integer/
"""


def reverse(x: int) -> int:
    # Reverse x
    x = str(x)
    if x[0] == '-':
        x = int('-' + x[::-1][:-1])
    else:
        x = int(x[::-1])
    # Check if x is outside the signed 32-bit integer range
    if -2 ** 31 <= x <= 2 ** 31:
        return x
    else:
        return 0


def main():
    test_cases = [
        123,
        -123,
        120,
        1534236469
    ]
    for num in test_cases:
        print(reverse(num))


if __name__ == '__main__':
    main()
