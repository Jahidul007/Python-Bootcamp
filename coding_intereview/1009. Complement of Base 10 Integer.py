class Solution:
    def bitwiseComplement(self, N: int) -> int:
        num = bin(N)[2:]
        ans = ''
        for i in num:

            if i == "1":
                ans += '0'
            else:
                ans += '1'
        ans = int(ans, 2)
        return ans
