class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        words = ''.join(words)
        letterCounter  = Counter(words)
        
        print(letterCounter )
        for letter in letterCounter:
            if letterCounter[letter] % n !=0:
                return False
        return True
