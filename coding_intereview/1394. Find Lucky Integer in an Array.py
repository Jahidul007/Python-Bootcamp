class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = set(arr)
        max = 0
        for i in dic:
            count = 0
            for j in range(len(arr)):
                if i == arr[j]:
                    count += 1
            if i == count:
                max = i
        if max > 0:
            return max
        else:
            return -1
