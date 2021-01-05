class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: (-x[1], x[0]))
        count = 0
        
        i = 0
        while i < len(boxTypes) and truckSize > 0:
            if boxTypes[i][0] <= truckSize:
                truckSize -= boxTypes[i][0]
                count += boxTypes[i][0] * boxTypes[i][1]
            else:
                count += truckSize * boxTypes[i][1]
                truckSize -= truckSize
                
            i += 1
                
        return count
