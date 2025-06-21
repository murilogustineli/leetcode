"""
https://leetcode.com/problems/valid-palindrome/
"""


def isPalindrome(s):
    # Converting uppercase letters into lowercase and removing non-alphanumeric characters
    pal = ''
    for i in s:
        if i.isalnum():
            pal += i.lower()

    for i in range(len(pal)):
        if pal[i] == pal[-i - 1]:
            continue
        else:
            return False
    return True


def is_palindrome_pointers(s):
    l, r = 0, len(s)-1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True


def main():
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "0P"
    ]
    for string in test_cases:
        print(isPalindrome(string))
        print(is_palindrome_pointers(string))


if __name__ == '__main__':
    main()
