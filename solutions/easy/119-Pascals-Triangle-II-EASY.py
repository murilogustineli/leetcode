"""
https://leetcode.com/problems/pascals-triangle-ii/
"""


def getRow(row):
    ans = [[1]]
    for i in range(1, row+1):
        temp1 = ans[-1] + [0]
        temp2 = [0] + ans[-1]
        var, pascal = 0, []
        for j in range(len(temp1)):
            var = temp1[j] + temp2[j]
            pascal.append(var)
        ans.append(pascal)

    return ans[-1]


def main():
    test_cases = [
        3,
        1,
        0,
        7
    ]
    for num in test_cases:
        print(getRow(num))


if __name__ == '__main__':
    main()
