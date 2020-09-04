class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ns = set(range(n))
        for i,j in edges:
            if j in ns: ns.remove(j)
                 
        return list(ns)
