class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wo = ''
        ws = ''
        for i in range( len(word1)):
            wo +=word1[i]
        for i in range( len(word2)):
            ws +=word2[i]
        if wo ==ws:
            return True
