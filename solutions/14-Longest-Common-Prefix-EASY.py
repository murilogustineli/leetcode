"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""


# ['flower', 'flow', 'flight']
# compare first letter of first word with first letter of second word
# create temp variable to store letter
## if both letters are the same -> continue
## else -> break


def commonPrefix(strs):
    res = ""
    shortest = min(strs, key=len)
    for i in range(len(shortest)):
        for j in range(len(strs)):
            if strs[j][i] != shortest[i]:
                return res
        res += shortest[i]
    return res


def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


if __name__ == '__main__':
    strs = [
        (['flower', 'flow', 'flight']),
        (["a"]),
        (['dog', 'racecar', 'car']),
        ([""])
    ]

    for lst in strs:
        print(longestCommonPrefix(lst))

    for lst in strs:
        print(commonPrefix(lst))
