class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        t=1
        cands=set()
        while t<=1000000000:
            tt=sorted([ttt for ttt in str(t)])
            cands.add(''.join(tt))
            t*=2
        print(cands)
        tt=sorted([ttt for ttt in str(N)])
        print(tt)
        return ''.join(tt) in cands