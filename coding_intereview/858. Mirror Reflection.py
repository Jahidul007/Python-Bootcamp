class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd = math.gcd(p, q)
        print(gcd)
        p //= gcd
        q //= gcd
        if q % 2 == 0:
            return 0
        return 2 if p % 2 == 0 else 1