class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        ans = []
        for i in range(l - 1):
            arr_r = max(arr[i + 1:])
            ans.append(arr_r)
        ans.append(-1)
        return ans