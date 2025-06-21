"""
https://leetcode.com/problems/add-binary/
"""


def addBinary(a, b):
    output = bin(int(a, 2) + int(b, 2))
    return output.split('b')[1]


def main():
    a, b = '11', '1'
    print(addBinary(a, b))


if __name__ == '__main__':
    main()
