class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        best,esum,total = 0,0,0
        for x in reversed(satisfaction):
            esum  += x
            total += esum
            if total>best:
                best = total
            elif esum<0:
                break
        return best

