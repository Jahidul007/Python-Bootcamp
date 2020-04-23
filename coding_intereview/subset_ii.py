class Solution(object):
    def subsetsWithDup(self, nums):

        nums.sort()
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
print(Solution().subsetsWithDup([1,2,2]))