from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        l = len(nums)
        if t == 0 and l == len(set(nums)):
            return False

        for i in range(l):
            for j in range(i + 1, i + k + 1):
                if j < l and abs(nums[i] - nums[j]) <= t:
                    return True
        return False