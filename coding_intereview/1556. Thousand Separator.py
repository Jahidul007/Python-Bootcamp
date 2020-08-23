class Solution:
    def thousandSeparator(self, n: int) -> str:
        st = (str(n))
        
        print(st)
        
        res = []
        for i in range(len(st)):
            if i>0 and (len(st)-i)%3==0:
                res.append('.')
            res.append(st[i])
        return "".join(res)
