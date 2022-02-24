"""
https://leetcode.com/problems/palindrome-number/
"""


def palindrome_loop(string):
    string = str(string)
    j = -1

    for i in range(len(string)//2):
        if string[i] == string[j]:
            j -= 1
            continue
        else:
            return 'no'

    return 'yes'


def palindrome(string):
    string = str(string)
    inv = string[::-1]

    if string == inv:
        return 'true'
    else:
        return 'false'


def main():
    test_cases = {
        ('rotor'),
        (101),
        ('10000001'),
        ('Hannah'),
        (100000000000010000000000001)
    }
    for i in test_cases:
        print(palindrome_loop(i))

    print()
    test = [
        (121),
        (-121),
        (10)
    ]
    for i in test:
        print(palindrome(i))


if __name__ == '__main__':
    main()
