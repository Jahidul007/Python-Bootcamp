class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        if n == 4:
            return n
        result = 1
        while n > 4:
            result *= 3
            n -= 3
        result *= n
        return result
