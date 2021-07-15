class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0;
        maxl = arr[0]
        for i in range(len(arr)):
            if arr[i]>maxl:
                maxl = arr[i]
            if i ==maxl:
                count+=1
        return count
