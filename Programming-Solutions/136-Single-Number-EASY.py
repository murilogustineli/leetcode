"""
https://leetcode.com/problems/single-number/
"""


def singleNumber(nums):
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    return min(dic, key=dic.get)


def main():
    test_cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1]
    ]
    for test in test_cases:
        print(singleNumber(test))


if __name__ == '__main__':
    main()
