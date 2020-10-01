class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ver = []
        hor = []
        res = 0
        for i in grid:
            hor.append(max(i))
        for i in zip(*grid):
            ver.append(max(i))
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                res += min(hor[i], ver[j]) - grid[i][j]
        return res
            
