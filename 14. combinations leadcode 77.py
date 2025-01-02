'''
https://leetcode.com/problems/combinations/description/
'''
#%%
from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        all_sub = []
        def backtrack(start=0, temp=[]):
            if len(temp)==k:
                all_sub.append(temp[:])
                return

            for i in range(start+1, n+1):
                temp.append(i)
                backtrack(i)# i is already 1 increased
                temp.pop()
        
        backtrack()
        return all_sub

s = Solution()
# %%
s.combine(4, 2)
# %%
