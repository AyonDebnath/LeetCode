from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # base case, search the boarders.

                # If a match is not found check the next element in the board
                j+=1
            i+=1
