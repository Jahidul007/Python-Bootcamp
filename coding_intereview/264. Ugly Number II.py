class Solution:
    def nthUglyNumber(self, n: int) -> bool:
        nums = [1]
        idx_2, idx_3, idx_5 = 0, 0, 0
        for i in range(n - 1):
            next2 = nums[idx_2] * 2
            next3 = nums[idx_3] * 3
            next5 = nums[idx_5] * 5
            next = min(next2, next3, next5)
            nums.append(next)
            if next == next2:
                idx_2 += 1
            if next == next3:
                idx_3 += 1
            if next == next5:
                idx_5 += 1
        return nums[-1]

