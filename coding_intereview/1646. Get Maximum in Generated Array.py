class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n ==0:
            return 0
        ls = [0,1]
        for i in range(2, n+1):
            if i%2== 0:
                ls.append(ls[i//2])
            else:
                ls.append(ls[i//2]+ls[i//2 + 1])
        return max(ls)
