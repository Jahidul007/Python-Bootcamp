class Solution:
    def groupThePeople(self, groupSize: List[int]) -> List[List[int]]:
        lis = [[]]*(len(groupSize)+1)
        res = []
        for i in range(len(groupSize)):
            if len(lis[groupSize[i]]) == groupSize[i]:
                res.append(lis[groupSize[i]])
                lis[groupSize[i]] = [i]
            else:
                lis[groupSize[i]] = lis[groupSize[i]]+[i]
        for i in lis:
            if i!=[]:
                res.append(i)
        return res
