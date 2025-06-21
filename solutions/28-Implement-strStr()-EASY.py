"""
https://leetcode.com/problems/implement-strstr/
"""


def strStr(haystack, needle):
    if needle in haystack and len(needle) >= 1:
        return haystack.find(needle)
    elif needle in haystack:
        return 0
    else:
        return -1


def strStr2(haystack, needle):
    nl, ml = len(needle), len(haystack)
    if nl == 0:
        return nl
    if ml < nl:
        return -1
    for i in range(ml - nl + 1):
        if haystack[i:i + nl] == needle:
            return i
    return -1


if __name__ == '__main__':
    haystack = ['hello', 'aaaaa', "", "", "a", "mississippi"]
    needle = ['ll', 'bba', "", "a", "", "issip"]

    for word in range(len(haystack)):
        print(strStr(haystack[word], needle[word]))
        # print(strStr2(haystack[word], needle[word]))
