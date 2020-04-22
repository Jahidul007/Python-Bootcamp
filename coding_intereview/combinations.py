class Solution(object):
    def combine(self, n, k):
        def recurse(i, li):
            if len(li) == k:
                result.append([x for x in li])
                return
            if i > n:
                return

            recurse(i + 1, li + [i])
            recurse(i + 1, li)

        result = []
        recurse(1, [])
        return result


print(Solution().combine(4, 2))
