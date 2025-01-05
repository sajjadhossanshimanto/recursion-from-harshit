# https://leetcode.com/problems/sudoku-solver/

#%%
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, column = len(board), len(board[0])
        def is_valid(x, y, ele) -> bool:
            # column checking
            for i in range(row):
                if board[i][y]==ele: return False
            
            # row checking
            for j in range(column):
                if board[x][j]==ele: return False
            
            start_row, start_col = (x // 3) * 3, (y // 3) * 3
            for i in range(start_row, start_row+3):
                for j in range(start_col, start_col+3):
                    if board[i][j] == ele: return False
            
            return True

        def backtrack(x=0, y=0):# starting x, y
            if y>8: return backtrack(x+1, 0)
            if x==9: return True
            
            if board[x][y]!=".": return backtrack(x, y+1)

            for num in range(1, 9+1):
                if not is_valid(x, y, str(num)): continue
                
                board[x][y] = str(num)
                if backtrack(x, y+1): return True
                board[x][y] = "."
            
            return False

        backtrack()

s = Solution()
# %%
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s.solveSudoku(board)
print(board)
# %%
