class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ft = []
        for i in range(1, n + 1):
            if n % i == 0:
                ft.append(i)
        if len(ft) >= k:
            return ft[k - 1]
        else:
            return -1
