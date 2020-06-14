class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        common = counter.most_common()
        print(common[-1][1])

        return common[0][0]