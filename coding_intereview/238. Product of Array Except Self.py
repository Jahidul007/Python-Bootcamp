class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        b = []

        if 0 not in nums:

            for i in range(len(nums)):
                a = a * nums[i]
            print(a)

            for i in range(len(nums)):
                c = int(a / nums[i])
                b.append(c)
            return b
        else:
            for i in range(len(nums)):
                if nums[i] != 0:
                    a = a * nums[i]
            for i in range(len(nums)):
                if nums[i] != 0:
                    b.append(0)
                elif nums.count(0) > 1:
                    b.append(0)
                else:
                    b.append(a)
            return b
