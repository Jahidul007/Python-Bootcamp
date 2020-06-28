class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        pair = collections.Counter([a % k for a in arr])
        for i in range(k):
            if i == 0:
                if pair[i] % 2 != 0:
                    return False
            else:
                if pair[k - i] != pair[i]:
                    return False
        return True
