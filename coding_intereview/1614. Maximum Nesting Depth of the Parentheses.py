class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cur = 0
        for i in s:
            if i =="(":
                cur+=1
                res = max(cur,res)
            if i ==")":
                cur-=1
        return res
