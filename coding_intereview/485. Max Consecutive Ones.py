class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0:
                if count > max1:
                    max1 = count
                count = 0
        if count > max1:
            max1 = count
        return max1
