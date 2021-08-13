class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        list_key = []
        for i,j in counter.items():
            list_key.append(j)
        for i in range(len(list_key)-1):
            if(list_key[i] != list_key[i+1]):
                return False
        return True
            
