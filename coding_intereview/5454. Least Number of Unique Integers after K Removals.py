class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        common = counter.most_common()
        print(common[-1][1])
        while common and k >= common[-1][1]:
            k -= common.pop()[1]
        return len(common)