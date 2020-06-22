class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(item for item in A if item % 2 == 0)
        ans = []

        for x, y in queries:
            if A[y] % 2 == 0 and x % 2 == 0:
                s += x
            if A[y] % 2 == 0 and x % 2 != 0:
                s -= A[y]
            if A[y] % 2 != 0 and x % 2 != 0:
                s += (A[y] + x)

            A[y] += x
            ans.append(s)
        return ans
