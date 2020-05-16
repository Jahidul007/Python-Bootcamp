class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        def setMax(nums):
            _max = max(nums)
            for i, num in enumerate(nums):
                if num == _max:
                    nums[i] = float('-inf')
            return _max

        max1 = setMax(nums)
        max2 = setMax(nums)
        max3 = setMax(nums)
        return max3 if max3 != float('-inf') else max(max1, max2)

