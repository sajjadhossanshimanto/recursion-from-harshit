'''
https://leetcode.com/problems/combination-sum-ii/description/
- can't use samne item twice
- res should not contain dublicate as
- input may contain dulicate
'''
#%%
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def backtrack(start: int, pre_sum: int, path: list) -> list[int, list]:
            if pre_sum>target: return
            elif pre_sum==target:
                res.append(path[:])
                return
            
            prev = None
            for pos in range(start, len(candidates)):
                if prev == candidates[pos]: continue
                prev = candidates[pos]

                path.append(candidates[pos])
                backtrack(pos+1, pre_sum+path[-1], path)
                path.pop()

        backtrack(0, 0, [])
        return res

s = Solution()
# %%
# [ [1,1,6], [1,2,5], [1,7], [2,6] ]
s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
# %%
# [ [1,2,2], [5] ]
s.combinationSum2(candidates = [2,5,2,1,2], target = 5)