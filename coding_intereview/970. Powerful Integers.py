class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a, b = 0, 0
        res = []
        if x == 1 and y == 1:
            if bound >= 2:
                res.append(2)
        elif x == 1:
            while y ** b + 1 <= bound:
                res.append(y ** b + 1)
                b += 1
        elif y == 1:
            while x ** a + 1 <= bound:
                res.append(x ** a + 1)
                a += 1
        else:
            while x ** a + 1 <= bound:
                if x ** a + y ** b <= bound:
                    res.append(x ** a + y ** b)
                    b += 1
                else:
                    a += 1
                    b = 0
        return list(set(res))

