class Solution:
    def countPrimeSetBits(self, l: int, r: int) -> int:

        def is_prime(num):

            if num == 1:
                return False
            elif num <= 3:
                return True
            for x in range(2, num - 1):
                if num % x == 0:
                    return False
            return True

        result = []
        cnt = 0
        for i in range(l, r + 1):
            if is_prime(bin(i).count("1")) == True:
                cnt += 1
        return cnt
        print(result)
