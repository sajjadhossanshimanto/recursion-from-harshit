# https://leetcode.com/problems/generate-parentheses/description/

#%%
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(open_counter=0, closed_counter=0, path=[]):
            if open_counter==closed_counter==n:
                t = "".join(path)
                if not res or res[-1]!=t:
                    res.append(t)
                return
            # if open_counter>n or closed_counter>n: return
            
            if open_counter<n:
                path.append("(")
                backtrack(open_counter+1, closed_counter, path)
                path.pop()
            if open_counter>closed_counter:
                c=0
                for _ in range(open_counter-closed_counter):
                    path.append(")")
                    c+=1
                    backtrack(open_counter, closed_counter+c, path)
                for _ in range(c):
                    path.pop()
            

        backtrack()
        return res

s = Solution()
# %%
# ["((()))","(()())","(())()","()(())","()()()"]
s.generateParenthesis(3)
# %%
s.generateParenthesis(4)
