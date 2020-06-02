class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        r = [1, 9, 9 * 9, 9 * 9 * 8, 9 * 9 * 8 * 7, 9 * 9 * 8 * 7 * 6, 9 * 9 * 8 * 7 * 6 * 5, 9 * 9 * 8 * 7 * 6 * 5 * 4,
             9 * 9 * 8 * 7 * 6 * 5 * 4 * 3, 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2, 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1]
        return sum(r[: n + 1])
