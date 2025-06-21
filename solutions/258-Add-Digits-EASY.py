"""
https://leetcode.com/problems/add-digits/
"""


def addDigits(num):
    num = str(num)
    n = ""
    while len(n) != 1:
        n = str(sum([int(i) for i in num]))
        num = n
    return int(n)


if __name__ == '__main__':
    print(addDigits(38))
