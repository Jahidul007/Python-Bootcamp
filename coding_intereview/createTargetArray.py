class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        output = []
        for i in range(len(index)):
            val = index[i]
            output.insert(val, nums[i])
        return output

