class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1:
            return True
        if n % 2 == 1:
            return False
        if n <= 0:
            return False

        while True:
            n = n // 2
            return (Solution().isPowerOfTwo(n))



print(Solution().isPowerOfTwo(27))
