'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
#%%
from typing import List
from itertools import permutations

key_map = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        def backtrack(index=0, path=[]):
            if index==len(digits):
                res.append("".join(path))
                return
            
            for i in key_map[digits[index]]:
                path.append(i)
                backtrack(index+1, path)
                path.pop()
        
        backtrack()
        return res

s = Solution()
#%%
s.letterCombinations("23")
# %%
