import math


class Solution:
    # method 1 O(n^2)
    def trailingZeroes(self, n: int) -> int:
        factorial = 1
        if int(n) >= 1:
            for i in range(1, int(n) + 1):
                factorial = factorial * i
        num = str(factorial)
        print(num)
        count = 0
        for i in range(len(num) - 1, 0, -1):
            if num[i] == "0":
                count += 1
            else:
                break
        return count

    # method 2 O(n)
    def trailingZeroes(self, n: int) -> int:
        x = 5
        count = 0
        while x <= n:
            count += n // x
            x *= 5
        return count

