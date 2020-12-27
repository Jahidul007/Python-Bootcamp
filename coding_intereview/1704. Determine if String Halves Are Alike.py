class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        num_vowels=0
        num_vowels1=0
    
        split = -( ( -len(s) )//2 )
        p1, p2 = s[:split], s[split:]
        for char in p1:
            if char in "aeiouAEIOU":
                num_vowels = num_vowels+1
        for char in p2:
            if char in "aeiouAEIOU":
                num_vowels1 = num_vowels1+1
        return num_vowels== num_vowels1
