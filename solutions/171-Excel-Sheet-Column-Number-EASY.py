"""
https://leetcode.com/problems/excel-sheet-column-number/
"""


def titleToNumber(columnTitle):
    ans, pos = 0, 0
    for letter in reversed(columnTitle):
        digit = ord(letter) - 64
        ans += digit * 26 ** pos
        pos += 1

    return ans


def main():
    test_cases = [
        "A",  # 1
        "B",  # 2
        "AA",  # 27
        "AB",  # 28
        "ZA",  # 677
        "ZY",  # 701
        "AAA",  # 703
        "FAB",  # 4084
        "ZAA",  # 17603 (26*26*26+27)
        "FXSHRXW"  # 2,147,483,647
    ]
    for string in test_cases:
        print(titleToNumber(string))


if __name__ == '__main__':
    main()
