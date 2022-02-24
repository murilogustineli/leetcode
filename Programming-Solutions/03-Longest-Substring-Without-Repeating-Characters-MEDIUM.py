"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def lengthOfLongestSubstring(s):
    strSet = set()
    start = output = 0

    for index in range(len(s)):
        while s[index] in strSet:
            strSet.remove(s[start])
            start += 1
        strSet.add(s[index])
        output = max(output, index - start + 1)
    return output


def main():
    test_cases = [
        'pwwkew',
        'abcabcbb',
        'bbbbbbb',
        'dvdf',
        'ckilbkd',
        'abba',
        'abac',
        '',
        'x'
    ]
    for s in test_cases:
        print(lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
