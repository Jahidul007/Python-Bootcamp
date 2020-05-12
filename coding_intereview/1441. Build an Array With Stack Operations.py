class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        pos = 0
        for i in range(1,n+1):
            if target[pos] == i:
                res.append("Push")
                pos +=1
                if pos>= len(target):
                    break
            else:
                res.append("Push")
                res.append("Pop")
        return res