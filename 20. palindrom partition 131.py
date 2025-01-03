'''
- key word "every substring" thats refers we need to generate all sub-set
- for generating sub-set we will use backtrack
# unique question
- instade of choising which one to keep 
- here we need to decide where to partition
'''
#%%
def is_palindrom(s, l, r):
    ''' both end points are inclusive '''
    # if l==r: return True
    while l<=r:
        if s[l]!=s[r]: return False
        l+=1
        r-=1
    
    return True

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def backtrack(start=0, path=[]):
            if start==len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                if not is_palindrom(s, start, i): continue

                path.append(s[start:i+1])
                backtrack(i+1, path)
                path.pop()

        backtrack()
        return res

s = Solution()
# %%
s.partition("aab")
# %%
