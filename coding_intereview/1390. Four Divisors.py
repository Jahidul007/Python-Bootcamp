class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        val = 0

        def fact(n):
            ft = set()
            for i in range(1, int(j ** 0.5) + 1):
                if j % i == 0:
                    ft.add(i)
                    ft.add(j // i)
                    if len(ft) > 4:
                        return 0
            if len(ft) == 4:
                return sum(ft)
            else:
                return 0

        for j in nums:
            val += fact(j)
        return val
