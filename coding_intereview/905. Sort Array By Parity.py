class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                ans.append(A[i])

        return ans + sorted([i for i in A if i not in ans])
