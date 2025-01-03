'''
https://leetcode.com/problems/permutations/
- it is guranted that `nums` cointain only distinc element
'''
#%%
from typing import List


'''
permutation of any number is n!
- array of length 3 will have 3! permutations
- so the callback stack is of n!

cloning an array taken O(n)
is included takes O(n)

total = n*n*n!
we can improve the is included checking
- 
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path=[], visit = [0]*len(nums)):
            if len(path)==len(nums):
                res.append(path[:])
            
            for i in range(len(nums)):
                if visit[i]: continue
                visit[i] = 1

                path.append(nums[i])
                backtrack(path)
                path.pop()
                visit[i] = 0

        backtrack()
        return res

s= Solution()
#%%
#  [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
s.permute([1, 2, 3])
# %%
