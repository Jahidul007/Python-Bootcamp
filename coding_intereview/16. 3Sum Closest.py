class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closestSum = sys.maxsize

        for i in range(0, len(nums) - 2):
            j = i + 1
            l = len(nums) - 1
            while (j < l):
                sum = nums[i] + nums[j] + nums[l]
                if abs(sum - target) < abs(closestSum - target):
                    closestSum = sum
                elif sum < target:
                    j += 1
                else:
                    l -= 1
        return closestSum