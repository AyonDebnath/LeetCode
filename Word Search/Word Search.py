from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if r >= ROWS or c >= COLS or (r, c) in path :
                return False

            if i == len(word):
                return True

            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)

            return res



        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

                # If a match is not found check the next element in the board
                j+=1
            i+=1
