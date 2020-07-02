class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = {(0, 0)}
        current = [0, 0]
        for i in path:
            if i == 'N':
                current[1]-=1
            elif i == 'S':
                current[1]+=1
            elif i=='E':
                current[0]+=1
            else:
                current[0]-=1
            
            if tuple(current) in seen:
                return True
            seen.add(tuple(current))
        return False
