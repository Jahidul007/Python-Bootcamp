class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        right=0
        left=0
        for x in chips:
            if x % 2 == 0:
                left += 1
            else:
                right += 1
        return min(left, right)