'''
https://leetcode.com/problems/combination-sum-iii/description/
'''
#%%
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 9+1))

        res = []
        def backtrack(start=0, pre_sum=0, path=[]) -> list[int, list]:
            if pre_sum>n: return
            elif pre_sum==n and len(path)==k:
                res.append(path[:])
                return
            
            if len(path)>k: return # guard condition
            for pos in range(start, len(nums)):
                path.append(nums[pos])
                backtrack(pos+1, pre_sum+path[-1], path)
                path.pop()

        backtrack()
        return res

s = Solution()
# %%
# [[1,2,4]]
s.combinationSum3(k = 3, n = 7)
# %%
# [[1,2,6],[1,3,5],[2,3,4]]
s.combinationSum3(k = 3, n = 9)
# %%
s.combinationSum3(k = 4, n = 1)

# %%
