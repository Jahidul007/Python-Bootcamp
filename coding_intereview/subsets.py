class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]
        result = []

        def recurse(i, n, li):
            result.append([x for x in li])

            for j in range(i, n):
                li.append(nums[j])
                recurse(j + 1, n, li)
                li.pop()

        recurse(0, len(nums), [])
        res = []
        for i in result:
            if i not in res:
                res.append(i)
        return res
    # generate subset using a stack

    def subset(self, nums):
        if nums == []:
            return  [[]]

        result = [[]]

        while len(nums):
            temp_r = []
            x = nums.pop()
            for i in result:
                temp_r.append(i + [])
                temp_r.append(i + [x])
            result = [item for item in temp_r]
        return result

print(Solution().subset([1,2,2]))