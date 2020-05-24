class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                dist = i - d[nums[i]]
                if dist <= k:
                    return True
                d[nums[i]] = i

        return False