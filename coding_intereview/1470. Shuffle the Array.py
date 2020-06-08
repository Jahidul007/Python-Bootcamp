class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        i = 0
        while len(nums) > len(ans):
            ans.append(nums[i])

        return ans