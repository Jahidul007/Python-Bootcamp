class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        _len = len(nums)
        res = [-1] * _len
        for i in range(_len):
            for j in range(i + 1, _len * 2):
                if nums[j % _len] > nums[i]:
                    res[i] = nums[j % _len]
                    break
        return res
