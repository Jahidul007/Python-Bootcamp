class Solution:
    def triangleNumber(self, nums) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        n = len(nums)
        res = 0
        sum = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                sum = nums[i] + nums[j]
                left = j + 1
                right = n;
                while (left < right):
                    mid = left + (right - left) // 2
                    if (nums[mid] < sum):
                        left = mid + 1
                    else:
                        right = mid

                res += right - 1 - j
        return res


print(Solution().count_triangles([0,1,0,1]))