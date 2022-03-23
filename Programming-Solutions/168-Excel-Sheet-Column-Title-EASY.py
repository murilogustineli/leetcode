"""
https://leetcode.com/problems/excel-sheet-column-title/
"""
import string


def convertToTitle(x):
    z = dict((i, k) for i, k in enumerate(string.ascii_uppercase))
    ans = ""
    while x > 0:
        x -= 1
        y = x % 26
        x = x // 26
        ans = str(z[y]) + ans
    return ans


def main():
    test_cases = [
        1,
        28,
        701
    ]
    for num in test_cases:
        print(convertToTitle(num))


if __name__ == '__main__':
    main()
