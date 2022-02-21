"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

Input: s = "()"
Output: true
"""


def isValid(s):
    # Dictionary of parenthesis pairs
    dic = {'(': ')', '[': ']', '{': '}'}
    res = []
    # Iterate over each parenthesis in string
    for c in s:
        # Append parenthesis value to array if in dictionary
        if c in dic:
            res.append(c)
        # Check if parenthesis value corresponds to its key
        else:
            if len(res) and dic[res[-1]] == c:
                del res[-1]
            # Return False if parenthesis value is not in the dictionary
            else:
                return False
    # Return True is res list is empty
    return res == []


if __name__ == '__main__':
    strs = [
        '()[]{}',
        '{[()]}',
        '[)',
        '([)]',
        '(',
        "[]()(()"
    ]

    for string in strs:
        print(isValid(string))
