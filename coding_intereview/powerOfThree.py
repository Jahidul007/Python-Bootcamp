class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        threepower = 3 ** 100;
        if (n <= 0):
            return False;
        else:
            if (threepower % n == 0):
                return True;
            else:
                return False;



print(Solution().isPowerOfTwo(27))
