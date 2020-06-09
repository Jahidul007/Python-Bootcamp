class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        ans = set(nums)
        missing = []
        for i in range(1, len(nums)):
            if i not in ans:
                missing.append(i)
        if len(nums) not in ans:
            missing.append(len(nums))
        return missing
