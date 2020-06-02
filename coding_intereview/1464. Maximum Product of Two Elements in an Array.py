class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        value = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                pro = (nums[i] - 1) * (nums[j] - 1)
                if pro > value:
                    value = pro
        return value
