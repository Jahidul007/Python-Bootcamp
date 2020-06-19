class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        s = [str(i) for i in b]
        res = int("".join(s))
        return pow(a, res, 1337)
