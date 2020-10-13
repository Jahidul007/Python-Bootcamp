class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        for i in arr:
            xor.append(xor[-1]^i)
        ans = []
        for l, r in queries:
            ans.append(xor[r+1]^xor[l])
        return ans
