class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        indx = -1
        count = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                indx = i
                count += 1
        if count==0:
            return True
        
        if count == 1:
            if indx == 0 or indx == len(nums)-2:
                return True
            if nums[indx-1] < nums[indx+1] or(indx+2 < len(nums) and nums[indx] < nums[indx+2]):
                return True
            
        return False
