
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        val = 0
        for i in range(len(arr)-2):
            if arr[i+1]-arr[i] == arr[i+2]-arr[i+1]:
                val+=1
        if val == len(arr)-2:
            return True
        else:
            return False
