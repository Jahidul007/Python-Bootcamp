import heapq
class Solution:
    def validateSequence(self, heap):
        if len(heap) < 3: return True
        heapq.heapify(heap)
        first  = heapq.heappop(heap) 
        second =  heapq.heappop(heap)
        diff = second - first
        while heap:
            first = second
            second = heapq.heappop(heap)
            if second - first != diff: return False
        return True
    
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        
        ans = []
        for index in range( len(l)):
            ans.append(self.validateSequence( nums[l[index] : r[index]+1]))
        return ans
        
