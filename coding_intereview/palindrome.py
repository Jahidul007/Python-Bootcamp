import re
class Solution:
    def isPalindrome1(self, s: str) -> bool:
        return s == s[::-1]

        s = s.lower();
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

    def isPalindrome(self, s: str) -> bool:
        s = s.lower();
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]


print(Solution().isPalindrome('0p'))
