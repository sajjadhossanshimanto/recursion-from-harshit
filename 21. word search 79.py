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
        def dfs(x=0, y=0, pos=0, visit=[[0]*len(board[0]) for _ in range(len(board))]):
            if board[x][y]!=word[pos]:
                return False
            pos+=1

            if pos>=len(word): 
                return True

            for i, j in moves:
                cx, cy = x+i, y+j
                if cx<0 or cy<0 or cx>=len(board) or cy>=len(board[0]) or visit[cx][cy]: continue
                visit[cx][cy] = 1

                if dfs(cx, cy, pos, visit): 
                    return True
                visit[cx][cy] = 0

            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if dfs(x, y): 
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