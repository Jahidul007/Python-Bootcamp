class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)>1 and word[0].islower() and word[1].isupper():
            return False
        for i in range(1, len(word)-1):
            if word[i].isupper()^word[i+1].isupper():
                return False
        return True