class Solution:
    def generate(self, rowIndex: int) -> List[List[int]]:
        m = []
        for j in range(0, rowIndex):
            ans = [1] * (j + 1)
            for i in range(1, j):
                ans[i] = ans[i - 1] * (j - i + 1) // i
                print(ans[i], j)
            m.append(ans)
        return m
