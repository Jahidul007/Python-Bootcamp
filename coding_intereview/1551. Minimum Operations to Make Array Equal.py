class Solution:
    def minOperations(self, n: int) -> int:
        odd = 1
        count = 0
        while odd<n:
            count += (n-odd)
            odd +=2
        return count
