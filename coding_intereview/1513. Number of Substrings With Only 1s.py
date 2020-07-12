class Solution:
    def numSub(self, s: str) -> int:
        cont = s.split('0')
        cur = 0
        res = 0
        for i in s:
            if i =='0':
                cur = 0
            else:
                cur+=1
                res +=cur
        return res% (10**9+7)
