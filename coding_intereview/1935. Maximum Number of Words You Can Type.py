class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res = 0
        for w in text.split():
            if not set(w) & set(brokenLetters):
                res+=1
        return res
