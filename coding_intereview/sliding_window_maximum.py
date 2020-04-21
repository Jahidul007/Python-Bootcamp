from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        result = []

        if k >= len(nums):
            result.append(max(nums))
            return result
        for i in range(k):
            dq.append(nums[i])
        max_n = max(dq)
        result.append(max_n)

        for i in range(k, len(nums)):
            last_item = dq.popleft()
            dq.append(nums[i])
            if nums[i] >= max_n:
                max_n = nums[i]
            elif last_item == max_n:
                max_n = max(dq)
            result.append(max_n)
        return result
