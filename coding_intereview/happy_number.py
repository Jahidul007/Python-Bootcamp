class Solution(object):
    def isHappy(self, n):
        def sum_of_digits(num):
            sum = 0
            while num:    # num != 0
                sum += pow(num % 10, 2)
                print(sum)
                num //= 10

            return sum

        while n > 9:
            n = sum_of_digits(n)

        return n == 1 or n == 7

print(Solution().isHappy(19))