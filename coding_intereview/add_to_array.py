class Solution:
    def addToArrayForm(self,A,k):
        sum = 0
        n = len(A)
        print(n)
        for i in range(n):
            sum += A[i] * pow(10, n-i-1)
        return str(sum + k)


A = [1, 2, 0, 0]
print(Solution().addToArrayForm(A,34))
