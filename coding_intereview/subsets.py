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
        return result

print(Solution().subsets([1,2,3]))