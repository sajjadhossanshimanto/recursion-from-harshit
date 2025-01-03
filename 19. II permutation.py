'''
https://leetcode.com/problems/permutations-ii/
- only diff input might contain dublicates
- but result can't have any dublicate set
'''
#%%
from typing import List
from itertools import permutations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(path=[], visit = [0]*len(nums)):
            if len(path)==len(nums):
                res.append(path[:])
            
            prev = None
            for i in range(len(nums)):
                if visit[i] or prev==nums[i]: continue
                visit[i] = 1
                prev = nums[i]

                path.append(nums[i])
                backtrack(path)
                path.pop()
                visit[i] = 0

        backtrack()
        return res

s= Solution()
#%%
s.permuteUnique([1, 2, 3])
# %%
# [[1,1,2], [1,2,1], [2,1,1]]
s.permuteUnique([1, 2, 1])
# %%
