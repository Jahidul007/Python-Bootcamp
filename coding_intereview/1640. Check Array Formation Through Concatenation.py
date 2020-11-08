class Solution:
    def canFormArray(self, a: List[int], p: List[List[int]]) -> bool:
        mp = {x[0]: x for x in p}
        res = []
        
        for num in a:
            res += mp.get(num, [])
            
        return res == a
