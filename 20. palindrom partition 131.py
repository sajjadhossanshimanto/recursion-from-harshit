'''
- key word "every substring" thats refers we need to generate all sub-set
- for generating sub-set we will use backtrack
'''
#%%
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtrack(start=0, path=[]):
            res.append(path[:])
            for i in range(start, len(s)):
                path.append(s[i])
                backtrack(i+1, path)
                path.pop()

        backtrack()
        return res

s = Solution()
# %%
s.partition("aab")
# %%
