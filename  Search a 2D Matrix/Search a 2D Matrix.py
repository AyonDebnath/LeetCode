class Solution:

    def getRowCol(self, index, rowCount, colCount):
        if index > rowCount * colCount:
            raise "index out of bounds in getRowCol()"

        if (index+1) < colCount:
            row = 0
        else:
            row = (index) // colCount #correct

        col = index - colCount * row

        return row, col

    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        l, r = 0, (len(matrix) * len(matrix[0])-1)

        while l <= r:
            i = (l + r) // 2
            row, col = self.getRowCol(i, len(matrix), len(matrix[0]))
            if target > matrix[row][col]:
                l = i + 1
            elif target < matrix[row][col]:
                r = i - 1
            else:
                return True
        return False


sol = Solution()
print(sol.getRowCol(1, 2, 1,))
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
