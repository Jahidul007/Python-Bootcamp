class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        res1 = Counter(word1);
        res2 = Counter(word2);
        val = set(res1+res2)
        
        for key in val:
            if(abs(res1[key]-res2[key])>3):
                return False
        return True
