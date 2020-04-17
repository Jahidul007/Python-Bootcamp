class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        sum = 0
        for i in range(n-1):
            for j in range(i+1, n):
                sum = (nums[i] + nums[j])
                if sum == target:
                    return [i, j]


print(Solution().twoSum([2, 7, 11, 15], 13))
