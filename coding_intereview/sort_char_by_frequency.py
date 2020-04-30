class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        li = sorted([(count[i], i) for i in count], reverse=True)
        print(li)
        res = []
        for i, c in li:
            res.append(i * c)
        return ''.join(res)
