class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''.join(c[0] for c in takewhile(lambda x:
        all(x[0] == y for y in x), zip(*strs)))
        return res