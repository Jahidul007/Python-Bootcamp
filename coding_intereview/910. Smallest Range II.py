class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        arr = sorted(A)

        res = arr[-1] - arr[0]
        for i in range(len(arr) - 1):
            arr[i] += 2 * K
            res = min(res, max(arr[i], arr[-1]) - min(arr[0], arr[i + 1]))
        return res