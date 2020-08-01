class Solution:
    def numOfSubarrays(self, A):
        count = [1, 0]
        cur = res = 0
        for a in A:
            cur ^= a & 1
            res += count[1 - cur]
            count[cur] += 1
        return res % (10**9 + 7)
