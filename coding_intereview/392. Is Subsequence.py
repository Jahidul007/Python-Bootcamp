class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pS = 0
        pT = 0

        while pT < len(t) and pS < len(s):
            if s[pS] == t[pT]:
                pS += 1
                pT += 1
                continue
            else:
                pT += 1
        return pS == len(s)