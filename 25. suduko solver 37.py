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
from time import time
t1 = time()
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
s.solveSudoku(board)
t2 = time()
# print(board)
print(t2-t1)
# %%
board

# %%
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Define helper functions
        def get_box_index(row, col):
            return (row // 3) * 3 + (col // 3)

        def is_valid(num, row, col):
            box = get_box_index(row, col)
            return num not in row_sets[row] and num not in col_sets[col] and num not in box_sets[box]

        def place_number(num, row, col):
            board[row][col] = num
            row_sets[row].add(num)
            col_sets[col].add(num)
            box_sets[get_box_index(row, col)].add(num)

        def remove_number(num, row, col):
            board[row][col] = "."
            row_sets[row].remove(num)
            col_sets[col].remove(num)
            box_sets[get_box_index(row, col)].remove(num)

        def backtrack(index=0):
            if index == len(empty_cells):
                return True
            
            row, col = empty_cells[index]
            for num in map(str, range(1, 10)):
                if is_valid(num, row, col):
                    place_number(num, row, col)
                    if backtrack(index + 1):
                        return True
                    remove_number(num, row, col)
            return False

        # Initialize sets for rows, columns, and boxes
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        # Pre-fill the sets with existing numbers on the board
        empty_cells = []
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    row_sets[r].add(num)
                    col_sets[c].add(num)
                    box_sets[get_box_index(r, c)].add(num)

        # Start backtracking
        backtrack()

s = Solution()
# %%
