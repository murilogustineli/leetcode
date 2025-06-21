"""
https://leetcode.com/problems/pascals-triangle/
"""


def generate(num):
    ans = []

    for i in range(1, num+1):
        c, pascal = 1, []
        for j in range(1, i+1):
            pascal.append(c)
            c = c * (i-j)//j
        ans.append(pascal)
    return ans


def pascal_triangle(num):
    """
    :param num: int
    :return: list
    if numRows = 5
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    """
    res = [[1]]
    for i in range(1, num):
        temp1 = res[-1] + [0]
        temp2 = [0] + res[-1]
        var = []
        for j in range(len(temp1)):
            var.append(temp1[j] + temp2[j])
        res.append(var)
        # res.append([temp1[j] + temp2[j] for j in range(len(temp1))])
    return res[:num]


def main():
    test_cases = [
        5,
        1,
        0,
        7
    ]
    for num in test_cases:
        print(generate(num))
        print(pascal_triangle(num))


if __name__ == '__main__':
    main()
