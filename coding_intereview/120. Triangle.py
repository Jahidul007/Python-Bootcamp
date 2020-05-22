from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        triangle.reverse()
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j+1])
        return triangle[-1][0]