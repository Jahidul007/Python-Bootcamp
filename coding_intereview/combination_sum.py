class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        # combination sum using duplicates
        def rescue(i, li, s):
            if s == target:
                if li not in result:
                    result.append([x for x in li])
            if s > target or i == len(candidates):
                return
            # combination sum using without duplicates
            # rescue(i+1, li+[candidates[i]], s+candidates[i])
            rescue(i, li+[candidates[i]], s+candidates[i])
            rescue(i+1, li, s)
        rescue(0, [], 0)
        return result

print(Solution().combinationSum([2,3,6,7],7))