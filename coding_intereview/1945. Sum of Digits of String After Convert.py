class Solution:
    def getLucky(self, s: str, k: int) -> int:
      
        s1= ""
        for i in range(len(s)):
            s1+=str(ord(s[i]) - ord('a') + 1)
       
        for _ in range(k): 
            x = sum(int(ch) for ch in s1)
            s1 = str(x)
        return x
