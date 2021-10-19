class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0;
        limit = 0;
        for i in nums:
            for j in nums[limit:]:
                if(abs(i - j)==k):
                    count+=1
            limit+=1
        return count
