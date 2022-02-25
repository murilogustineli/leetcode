"""
https://leetcode.com/problems/climbing-stairs/
"""


def climbStairs(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b

    return b


def main():
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in test_cases:
        print(climbStairs(i))


if __name__ == '__main__':
    main()
