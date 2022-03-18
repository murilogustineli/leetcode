"""
https://leetcode.com/problems/subrectangle-queries/
"""


class SubrectangleQueries:
    def __init__(self, rectangle):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]


def main():
    global obj
    test_cases = [
        (["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue", "updateSubrectangle",
          "getValue", "getValue"],
         [[[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]],
          [0, 2],
          [0, 0, 3, 2, 5],
          [0, 2],
          [3, 1],
          [3, 0, 3, 2, 10],
          [3, 1], [0, 2]]),
        (["SubrectangleQueries", "getValue", "updateSubrectangle", "getValue", "getValue", "updateSubrectangle",
          "getValue"],
         [[[1, 1, 1], [2, 2, 2], [3, 3, 3]],
          [0, 0],
          [0, 0, 2, 2, 100],
          [0, 0],
          [2, 2],
          [1, 1, 2, 2, 20],
          [2, 2]])
    ]
    output = []
    for array in test_cases:
        iteration = []
        for string in range(len(array[0])):
            if array[0][string] == "SubrectangleQueries":
                rectangle = array[1][0]
                obj = SubrectangleQueries(rectangle)
                iteration.append('null')
            elif array[0][string] == "getValue":
                row = array[1][string][0]
                col = array[1][string][1]
                iteration.append(obj.getValue(row, col))
                # print(f"getValue: {obj.getValue(row, col)}")
            else:
                row1 = array[1][string][0]
                col1 = array[1][string][1]
                row2 = array[1][string][2]
                col2 = array[1][string][3]
                newValue = array[1][string][4]
                obj.updateSubrectangle(row1, col1, row2, col2, newValue)
                iteration.append('null')
                # print(f'update: {obj.updateSubrectangle(row1, col1, row2, col2, newValue)}')
        output.append(iteration)
    for i in output:
        print(i)


if __name__ == '__main__':
    main()


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
