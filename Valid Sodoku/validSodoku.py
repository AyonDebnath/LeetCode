class Solution:
    def isValidSudoku(self, board):
        numsAndCount = {}

        # Check for duplicates in the rows
        for i in range(10):
            numsAndCount[i] = 0

        for i in range(9):
            for j in range(9):
                if(board[i][j] != "."):
                    numsAndCount[int(board[i][j])] += 1
                    if numsAndCount[int(board[i][j])] > 1:
                        return False
            for k in range(10):
                numsAndCount[k] = 0

        # Check for duplicates in the column
        for i in range(9):
            for j in range(9):
                if (board[j][i] != "."):
                    numsAndCount[int(board[j][i])] += 1
                    if numsAndCount[int(board[j][i])] > 1:
                        return False
            for k in range(10):
                numsAndCount[k] = 0

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # Check for duplicates in the subbox
                for k in range(i, i+3, 1):
                    for l in range(j, j+3, 1):
                        if (board[k][l] != "."):
                            numsAndCount[int(board[k][l])] += 1
                            if numsAndCount[int(board[k][l])] > 1:
                                return False
                for k in range(10):
                    numsAndCount[k] = 0
        return True



sol = Solution()
print(sol.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
