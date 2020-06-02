class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:]
        ans = ''
        for i in num:

            if i == "1":
                ans += '0'
            else:
                ans += '1'
        ans = int(ans, 2)
        return ans