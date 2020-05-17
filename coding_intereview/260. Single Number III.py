class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        unique_set = set()
        for num in nums:
            if len(unique_set & set([num])):
                unique_set.remove(num)
            else:
                unique_set.add(num)
        return list(unique_set)