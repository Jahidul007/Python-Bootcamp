class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ''
        while n > 0:
            x = n % 26;
            print(x)
            if (x == 0):
                ans += ''.join('Z');
                n -= 1
            else:
                ans += ''.join(chr(ord('A') - 1 + x));
                print(ans)

            n //= 26;

        print(ans)
        return ans[::-1]