"""
https://leetcode.com/problems/summary-ranges/
"""


def summaryRanges(nums):
    ranges = []
    for i in nums:
        if ranges and ranges[-1][1] == i - 1:
            ranges[-1][1] = i
        else:
            ranges.append([i, i])
    return [f"{a}->{b}" if len(set([a, b])) > 1 else f"{a}" for a, b in ranges]


def main():
    test_cases = [
        [7],
        [0, 1, 2, 4, 5, 7],
        [0, 2, 3, 4, 6, 8, 9],
        [0, 1, 3, 4, 5, 7, 8, 9]
    ]
    for test in test_cases:
        print(summaryRanges(test))


if __name__ == '__main__':
    main()
