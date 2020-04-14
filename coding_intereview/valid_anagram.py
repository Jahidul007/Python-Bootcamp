import re
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sortString(s):
            strp = list(s)
            strp.sort()
            a = ''
            return a.join(strp)
        s = sortString(s)
        t = sortString(t)

        return s == t
print(Solution().isAnagram("s",""))

"""class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if s == '' and t == '':
            return True
        if len(s) != len(t):
            return False
        else:
            pattern = []
            target = []
            for i in range(len(s)):
                pattern.append(s[i])
                target.append(t[i])
                pattern.sort()
                target.sort()
                pat = ''
                tar = ''
                pat = pat.join(pattern)
                tar = tar.join(target)


        return pat == tar
"""
