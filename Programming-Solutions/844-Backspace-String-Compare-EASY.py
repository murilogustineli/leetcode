"""
https://leetcode.com/problems/backspace-string-compare/
"""


def backspaceCompare(s, t):
    s_arr, t_arr = [], []
    for i in range(len(s)):
        if s[i] == '#' and len(s_arr) > 0:
            s_arr.pop()
        elif s[i] != '#':
            s_arr.append(s[i])

    for i in range(len(t)):
        if t[i] == '#' and len(t_arr) > 0:
            t_arr.pop()
        elif t[i] != '#':
            t_arr.append(t[i])

    if s_arr == t_arr:
        return True
    return False


def main():
    test_cases = [
        ('ab#c', 'ad#c'),
        ('ab##', 'c#d#'),
        ('a#c', 'b'),
        ("a##c", "#a#c")
    ]
    for s, t in test_cases:
        print(backspaceCompare(s, t))


if __name__ == '__main__':
    main()
