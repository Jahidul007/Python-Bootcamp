class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        result = m & n
        diff = n - m
        bit = 1
        while bit <= diff:
            result &= ~bit
            bit *= 2
        return result
