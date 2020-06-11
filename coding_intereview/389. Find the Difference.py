class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        a = Counter(t) - Counter(s)
        return ''.join(sorted(a.elements()))