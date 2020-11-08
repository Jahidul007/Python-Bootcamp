class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi = 1
        count = 1
        for i in range (len(nums)-1):
            if nums[i+1]> nums[i]:
                count +=1
                maxi = max(maxi, count)
            else: 
                count = 1
        return maxi
                
