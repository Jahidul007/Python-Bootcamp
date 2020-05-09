class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indx =0
        for i in range(len(nums)):
            if(nums[i])!=0:
                nums[indx]=nums[i]
                indx+=1
        while(indx<len(nums)):
            nums[indx]=0
            indx+=1
        return nums