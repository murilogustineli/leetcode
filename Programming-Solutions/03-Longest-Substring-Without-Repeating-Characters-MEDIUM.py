"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


def lengthOfLongestSubstring(s):
    strSet = set()
    start = output = 0

    for idx in range(len(s)):
        while s[idx] in strSet:
            strSet.remove(s[start])
            start += 1
        strSet.add(s[idx])
        output = max(output, idx - start + 1)
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
