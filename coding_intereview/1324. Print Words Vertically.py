class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        sen = []
        maxLength = max(len(w) for w in words)
    
        for i in range(maxLength):
            current = []
            for w in words:
                current.append(w[i] if i < len(w) else " ")
            sen.append("".join(current).rstrip())
        return sen
            
