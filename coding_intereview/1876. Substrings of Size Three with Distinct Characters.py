class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0 
        for i in range(len(s)-2):
            word = s[i:i+3]
            if(len(set(word))== len(word)):
                count+=1
        return count
