class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        sum = 0
        min = 0
        for i in nums:
            sum += i
            if sum < min:
                min = sum

        return -(min) + 1
