class Solution:
    def topKFrequent(self, words, k: int) -> List[str]:
        counts = collections.Counter(words)
        li = sorted([(counts[i], i) for i in counts], reverse= True)
        print (li)
        res = []
        max = 0
        for i ,c in li:
            res.append(c)
            if len(res)==k:
                return res