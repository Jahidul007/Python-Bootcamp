class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(len(A)):
            for d in range(1, 4):
                if i + d < len(A) and A[i] == A[i + d]:
                    return A[i]
        return -1
