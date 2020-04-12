import math


class Solution:
    def mySqrt(self, x: int) -> int:
        if x >= 0:
            return int(math.sqrt(x))

    def mySqrt1(self, x):
        if x >= 0:
            for i in range(x):
                sq = i * i
                if sq == x:
                    return i
                if sq > x:
                    return i - 1


print(Solution().mySqrt1(10))
