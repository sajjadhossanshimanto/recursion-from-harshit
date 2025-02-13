# https://leetcode.com/problems/sudoku-solver/

#%%
from typing import List


class Solution:# 10 sec for hard test
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

class Solution:# 5 secound for hard test
    # optimisation: pre-generated empty cell
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
from typing import List

class Solution:# 1.32 sec
    # optimisation: 1. pre-generated cell_candidates list
    # solve in accordance 2. sorted cell_candidate
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Helper functions
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

        def get_candidates(row, col):
            box = get_box_index(row, col)
            candidates = set(str(num) for num in range(1, 10))
            return candidates - row_sets[row] - col_sets[col] - box_sets[box]

        def backtrack(index=0):
            if index == len(empty_cells):
                return True
            
            # Select the next cell dynamically based on the heuristic
            row, col = empty_cells[index]
            candidates = cell_candidates[index]
            
            for num in candidates:
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

        # Pre-fill the sets and identify empty cells
        empty_cells = []
        cell_candidates = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    row_sets[r].add(num)
                    col_sets[c].add(num)
                    box_sets[get_box_index(r, c)].add(num)

        # Precompute valid candidates for each empty cell
        for row, col in empty_cells:
            candidates = get_candidates(row, col)
            if not candidates:
                return  # No valid solution
            cell_candidates.append(sorted(candidates))

        # Sort cells by the number of candidates (heuristic)
        empty_cells = [cell for _, cell in sorted(zip(cell_candidates, empty_cells), key=lambda x: len(x[0]))]
        cell_candidates = sorted(cell_candidates, key=len)

        # Start backtracking
        backtrack()

s = Solution()

# %%
from typing import List

class Solution:
    # have all the previous optimisation with
    # Dynamic Ordering of Cells 
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying the board in-place.
        """
        # Track sets of numbers used in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize tracking sets and identify empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def get_candidates(r: int, c: int) -> set:
            """
            Returns the valid candidates for a given cell.
            """
            box_index = (r // 3) * 3 + (c // 3)
            all_numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
            return all_numbers - rows[r] - cols[c] - boxes[box_index]

        def backtrack(index: int) -> bool:
            """
            Backtracking function to solve the Sudoku puzzle.
            """
            if index == len(empty_cells):
                return True  # All cells are filled successfully

            # Find the next cell with the fewest candidates
            min_candidates = float('inf')
            min_index = index

            for i in range(index, len(empty_cells)):
                r, c = empty_cells[i]
                num_candidates = len(get_candidates(r, c))
                if num_candidates < min_candidates:
                    min_candidates = num_candidates
                    min_index = i
                if min_candidates == 1:  # Optimal case: only one candidate
                    break

            # Swap the cell with the fewest candidates to the current position
            empty_cells[index], empty_cells[min_index] = empty_cells[min_index], empty_cells[index]
            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)

            # Try each candidate for the current cell
            for num in get_candidates(r, c):
                # Place the number
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

                # Recurse to the next cell
                if backtrack(index + 1):
                    return True

                # Undo the placement
                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_index].remove(num)

            return False  # No valid solution found for this path

        # Start solving from the first empty cell
        backtrack(0)

s = Solution()
# %%
