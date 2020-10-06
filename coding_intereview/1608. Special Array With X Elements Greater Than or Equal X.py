class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i]>i:
                count += 1
        
        if count < len(nums) and count == nums[count]:
            return -1
        else:
            return count
        
