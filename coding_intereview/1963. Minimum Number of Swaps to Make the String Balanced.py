class Solution:
    def minSwaps(self, s: str) -> int:
        res = 0
        count = 0
        for value in s:
            if value == "[":
                count+=1
            else:
                count -=1
            res = min(res, count)
        return (-res+1)//2
