"""
https://leetcode.com/problems/happy-number/
"""


def isHappy(n):
    nums = [i for i in str(n)]
    counter = 0
    if int(nums[0]) > 0:
        while nums != '1' and counter < 1000:
            nums = sum([int(i)**2 for i in nums])
            nums = str(nums)
            counter += 1
        if nums == '1' and counter < 1000:
            return True
    return False


def main():
    test_cases = [
        19,
        2
    ]
    for i in test_cases:
        print(isHappy(i))


if __name__ == '__main__':
    main()
