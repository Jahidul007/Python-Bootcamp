class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0, len(nums), 2):
            output = output + (nums[i] * [nums[i + 1]])
        return output
