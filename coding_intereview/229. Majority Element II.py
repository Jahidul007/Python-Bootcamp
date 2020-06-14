class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        # common = counter.most_common()
        maximum = len(nums) / 3
        ans = []
        for i, j in counter.items():
            print(i, j)
            if j > maximum:
                ans.append(i)

        return ans
