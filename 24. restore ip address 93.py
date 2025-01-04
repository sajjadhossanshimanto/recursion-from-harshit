'''
https://leetcode.com/problems/restore-ip-addresses/
'''
#%%
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        def valid_ip(segment):
            # master checks. len>1 will both 00 as wll as 0 followed bya nay num
            if segment[0]=="0" and len(segment)>1: return False
            return 0<=int(segment)<=255

        def backtrack(start=0, path=[]):
            if len(path)==4 and start>=len(s):
                ips.append(".".join(path))
                return
            if len(path)>4: return

            for end in range(start+1, min(start+4, len(s)+1)):
                path.append(s[start: end])
                if valid_ip(path[-1]):
                    backtrack(end, path)
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
# %% corner case
# ["0.10.0.10","0.100.1.0"]
s.restoreIpAddresses("010010")
# %%
