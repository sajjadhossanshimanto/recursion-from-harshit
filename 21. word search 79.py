# https://leetcode.com/problems/word-search/description/

#%%
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x=0, y=0, path=[], visit=[[0]*len(board[0]) for _ in range(len(board))]):
            if x<0 or y<0 or x>=len(board) or y>=len(board[0]): 
                return False
            
            if visit[x][y]: return
            visit[x][y] = 1

            path.append(board[x][y])
            if "".join(path) == word: return True

            if dfs(x+1, y, path, visit): return True
            if dfs(x, y+1, path, visit): return True
            if dfs(x-1, y, path, visit): return True
            if dfs(x, y-1, path, visit): return True
            path.pop()
            visit[x][y] = 0

            return False

        return dfs(0, 0)



s = Solution()
# %%
s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
# %%
s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
#%%
s.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
# %%
