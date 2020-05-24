class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for i in range(len(nums)):
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = True
        return False
