class Solution:
    def titleToNumber(self, s: str) -> int:
        number = 0
        for i in range(len(s)):
            number=number*26 + ord(s[i])-64
        return number