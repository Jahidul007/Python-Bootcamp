class Solution:
    def maxPower(self, s: str) -> int:
        max1 = 0
        count = 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                count += 1
            else:
                if count > max1:
                    max1 = count
                count = 1
        if count > max1:
            max1 = count
        return max1
