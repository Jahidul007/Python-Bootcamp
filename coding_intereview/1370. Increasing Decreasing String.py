class Solution:
    def sortString(self, s: str) -> str:
        str = sorted(set(s))

        lst = list(s)
        ans = ""
        while lst:
            for i in str:
                if i in lst:
                    ans += i
                    lst.remove(i)
            for i in str[::-1]:
                if i in lst:
                    ans += i
                    lst.remove(i)
        return ans
