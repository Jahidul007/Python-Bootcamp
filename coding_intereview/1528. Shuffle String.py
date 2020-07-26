class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = []
        for i in range(len(s)):
            for j in range(len(indices)):
                if indices[j]==i:
                    res.append(s[j])
            
        return ''.join(res)
