class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        x, y = 1, 1000
        while x <= 1000 and y >= 1:
            func = customfunction.f(x, y)
            if func > z:
                y -= 1
            elif func < z:
                x += 1
            else:
                res.append([x, y])
                x += 1
        return res
