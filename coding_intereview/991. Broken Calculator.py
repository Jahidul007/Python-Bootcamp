class Solution:
    def brokenCalc(self, x: int, y: int) -> int:
        if x >= y:
            return x - y
        if y % 2 == 0:
            return 1 + self.brokenCalc(x, y // 2)
        if y % 2 == 1:
            return 1 + self.brokenCalc(x, y + 1)
