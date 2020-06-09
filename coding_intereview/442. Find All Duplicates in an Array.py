class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup = []
        value = {}
        for i in nums:
            if i in value:
                dup.append(i)
            else:
                value[i] = 1

        return dup
