'''
https://leetcode.com/problems/restore-ip-addresses/
'''
#%%
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        def backtrack(start=0, path=[]):
            if len(path)==4 and start>=len(s):
                ips.append(".".join(path))
                return
            if len(path)>4: return

            for end in range(start+1, min(start+4, len(s)+1)):
                path.append(s[start: end])
                if 0<=int(path[-1])<=255:
                    if int(path[-1])==0 or path[-1][0]!="0":
                        backtrack(end, path)
                        # continue# leading zero check
                path.pop()

        backtrack()
        return ips

s=Solution()
# %%
# ["255.255.11.135","255.255.111.35"]
s.restoreIpAddresses("25525511135")
# %%
# ["0.0.0.0"]
s.restoreIpAddresses("0000")
# %%
# ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
s.restoreIpAddresses("101023")
# %%
