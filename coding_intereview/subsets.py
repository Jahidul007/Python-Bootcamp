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
            return [[]]

        result = [[]]

        while len(nums):
            temp_r = []
            x = nums.pop()
            for i in result:
                temp_r.append(i + [])
                print(i, " temp= ", temp_r)
                temp_r.append(i + [x])

                print("temp2= ", temp_r)
            result = [item for item in temp_r]
        return result

    def subset3(self, nums):
        result = []
        subset_len = 2 ** len(nums)
        for num in range(subset_len):
            li = []
            for i in range(len(nums)):
                if num & (1 << i):
                    li.append(nums[i])
            print(li)
            result.append(li)
        return result


print(Solution().subset3([1, 2, 3]))
