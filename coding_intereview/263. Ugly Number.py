class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        if n % 2 == 0:
            return self.isUgly(n // 2)
        if n % 3 == 0:
            return self.isUgly(n // 3)
        if n % 5 == 0:
            return self.isUgly(n // 5)
        if n == 1:
            return True
