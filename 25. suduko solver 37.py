# https://leetcode.com/problems/sudoku-solver/

#%%
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, column = len(board), len(board[0])
        def is_valid(x, y) -> List:
            ele = board[x][y]
            
            # column checking
            for i in range(row):
                if board[i][y]==ele: return False
            
            # row checking
            for j in range(column):
                if board[x][j]==ele: return False
            
            cell = (x//3)*3
            for i in range(cell, cell+3):
                for j in range(cell, cell+3):
                    if board[i][j] == ele: return False
            
            return True

        def backtrack():
            pass



s = Solution()
# %%
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)