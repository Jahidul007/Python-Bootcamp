class Solution:
    def arrangeCoins(self, n: int) -> int:
        level = 0
        count = 0
        while count + level + 1 <= n:
            level += 1
            count += level
        return level