# https://leetcode.com/problems/word-search/description/

#%%
from typing import List


moves = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, column = len(board), len(board[0])

        # note: same as declearing it as paramiter. as it only decleared once
        visit=[[0]*len(board[0]) for _ in range(len(board))]
        def dfs(x=0, y=0, index=0):
            if index==len(word): 
                return True

            if x<0 or y<0 or x>=row or y>=column or visit[x][y] or board[x][y]!=word[index]:
                return False
            visit[x][y] = 1

            for i, j in moves:
                cx, cy = x+i, y+j
                if dfs(cx, cy, index+1): 
                    return True
            visit[x][y] = 0

        for x in range(row):
            for y in range(column):
                if dfs(x, y, 0):
                    return True
        
        return False




s = Solution()
# %%
s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
# %%
s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
#%%
s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
# %%
s.exist([["a"]], "a")
# %%
s.exist([["a","b"]], "ba")
# %%
s.exist([["a","a"]], "aaa")
# %%
