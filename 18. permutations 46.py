'''
https://leetcode.com/problems/permutations/
- it is guranted that `nums` cointain only distinc element
'''
#%%
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path=[]):
            if len(path)==len(nums):
                res.append(path[:])
            
            for i in range(len(nums)):
                if nums[i] in path: continue

                path.append(nums[i])
                backtrack(path)
                path.pop()

        backtrack()
        return res

s= Solution()
#%%
#  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
s.permute([1, 2, 3])
# %%
