class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A[0] > A[len(A) - 1]:
            A = A[::-1]
        cnt = 0
        for i in range(0, len(A) - 1):
            if A[i] <= A[i + 1]:
                cnt += 1
        print(cnt)
        if cnt == len(A) - 1:
            return True
