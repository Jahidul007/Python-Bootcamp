import itertools


class Solution:
    def permute(self, nums):
        # return list(itertools.permutations(nums))
        res = []

        def _backtrac(nums, prelist):

            if len(nums) <= 0:
                res.append(prelist)
            else:
                for i in nums:
                    p_list = prelist.copy()

                    p_list.append(i)

                    left_nums = nums.copy()
                    print(left_nums, p_list)
                    left_nums.remove(i)

                    _backtrac(left_nums, p_list)

        _backtrac(nums, [])
        return res


print(Solution().permute([1, 2, 3]))
