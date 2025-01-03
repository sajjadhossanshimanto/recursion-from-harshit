'''
https://leetcode.com/problems/combination-sum/description/
- one item can be used multiple time
'''
#%%
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        all_sub = []
        def backtrack(start: int=0, pre_sum: int=0, path=[]):
            if pre_sum>target: return
            if pre_sum==target:
                all_sub.append(path[:])
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, pre_sum+path[-1], path)
                path.pop()

        backtrack()
        return all_sub

s = Solution()
# %%
# Output: [[2,2,3], [7]]
s.combinationSum([2, 3, 6, 7], 7)
# %%
