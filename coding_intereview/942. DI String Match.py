class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low = 0
        high = n
        ans = []
        for i in range(n):
            if s[i]=="I":
                ans.append(low)
                low+=1
            else:
                ans.append(high)
                high -=1
        ans.append(low)
        return ans