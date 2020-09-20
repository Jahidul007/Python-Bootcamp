class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)
        for i in range (len(arr)):
            sum+= ((i + 1) * (n - i) + 1) // 2 * arr[i];
        return sum
