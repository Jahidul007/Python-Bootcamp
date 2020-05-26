class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        op = []
        a = [i for i in range(1,m+1)]
        for val in queries:
            i = a.index(val)
            op.append(i)
            a.insert(0,a.pop(i))
        return op