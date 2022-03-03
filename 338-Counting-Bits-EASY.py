"""
https://leetcode.com/problems/counting-bits/
"""


# Naive way
def countBits_naive(n):
    bit, ans = [], []
    for i in range(n + 1):
        bit.append(str(bin(i).split('b')[1]))

    for i in bit:
        count = 0
        if '1' in i:
            for j in i:
                if j == '1':
                    count += 1
            ans.append(count)
        else:
            ans.append(0)
    return ans


# Using slicing
def countBits_slicing(n):
    ans = [0]
    while len(ans) <= n:
        ans += [i + 1 for i in ans]
    return ans[:n + 1]


# Simple solution
def countBits(n):
    ans = []
    for i in range(n + 1):
        ans.append(int(bin(i)[2:].count('1')))
    return ans


def main():
    test_cases = [2, 5]
    for n in test_cases:
        print(countBits_naive(n))
        print(countBits_slicing(n))
        print(countBits(n))


if __name__ == '__main__':
    main()
