class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A = sum(A)
        sum_B = sum(B)
        for i in A:
            if i + (sum_B - sum_A) // 2 in B:
                return [i, i + (sum_B - sum_A) // 2]
