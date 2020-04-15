class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestStr = ''
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(longestStr):
                longestStr = temp

            temp = self.helper(s, i, i + 1)
            if len(temp) > len(longestStr):
                longestStr = temp
        return longestStr

    def helper(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start + 1:end]



print(Solution().longestPalindrome('babad'))
