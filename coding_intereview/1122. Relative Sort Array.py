class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    ans.append(arr1[j])

        return ans + sorted([i for i in arr1 if i not in arr2])