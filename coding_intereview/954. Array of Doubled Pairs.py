class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = collections.Counter(A)
        for x in sorted(cnt, key=abs):
            if cnt[x] > cnt[2 * x]:
                return 0
            cnt[2 * x] -= cnt[x]
        return 1