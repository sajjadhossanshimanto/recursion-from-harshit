# here we will think -> with which element can we form different subsets


all_subs = []
def subsets(l, index=0, temp=[]):
    # if index>len(l):
    #     return

    all_subs.append(temp[:])
    for i in range(index, len(l)):
        temp.append(l[i])
        subsets(l, i+1, temp)
        temp.pop()

subsets(["a", 'b', 'c'])
print(all_subs)


#%%
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        all_subs = []
        def backtrack(index=0, temp=[]):
            # if index>len(l):
            #     return

            all_subs.append(temp[:])
            for i in range(index, len(nums)):
                temp.append(nums[i])
                backtrack(i+1, temp)
                temp.pop()
        
        backtrack()
        return all_subs

# %%
Solution().subsets([1, 2, 3])
# %%
