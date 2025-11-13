from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if r >= ROWS or r < 0 or c >= COLS or c < 0 or (r, c) in path or word[i] != board[r][c]:
                return False

            if i == len(word)-1:
                return True

            path.add((r, c))
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r, c))
            return res



        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

                # If a match is not found check the next element in the board
                col+=1
            row+=1
        return False

sol = Solution()
print(sol.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))