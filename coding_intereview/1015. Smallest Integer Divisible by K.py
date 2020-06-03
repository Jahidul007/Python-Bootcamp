class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        if k == 1:
            return 1
        count =1
        n = 1
        while(n%k>0):
            n = (n%k)*10+1
            count +=1
        return count