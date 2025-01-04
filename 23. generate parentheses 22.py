# https://leetcode.com/problems/generate-parentheses/description/

#%%
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def backtrack(open_counter=0, closed_counter=0, opend: bool=False, path=[]):
            if open_counter==closed_counter==n:
                res.append("".join(path))
                return
            # if open_counter>n or closed_counter>n: return
            
            if open_counter<n:
                path.append("(")
                backtrack(open_counter+1, closed_counter, True, path)
                path.pop()
            if opend:
                if open_counter==n:
                    c=0
                    for _ in range(n-closed_counter):
                        path.append(")")
                        c+=1
                        # on every close i need to backtrack
                    backtrack(open_counter, closed_counter+c, False, path)
                    for _ in range(c):
                        path.pop()
                else:
                    path.append(")")
                    backtrack(open_counter, closed_counter+1, False, path)
                    path.pop()

        backtrack()
        return res

s = Solution()
# %%
# ["((()))","(()())","(())()","()(())","()()()"]
s.generateParenthesis(3)
# %%
