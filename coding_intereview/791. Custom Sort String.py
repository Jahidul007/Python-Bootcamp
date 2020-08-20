class Solution:
    def customSortString(self, S: str, T: str) -> str:
        cntr = collections.Counter(T)
        prefix = ""
        for c in S:
            prefix += c*cntr[c]
            del cntr[c]
        
        res = prefix
        for c in cntr:
            res += c*cntr[c]
        return res
