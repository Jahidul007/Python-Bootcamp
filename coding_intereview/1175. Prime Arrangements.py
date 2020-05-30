class Solution:
    def factorial(n: int) -> int:
        return n * factorial(n - 1) if n > 1 else 1

    def numPrimeArrangements(self, n: int) -> int:
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
        count = 0
        for i in primes:
            if i <= n:
                count += 1
            else:
                break
        return ((Solution.factorial(n - count) * Solution.factorial(count)) % (int(math.pow(10, 9)) + 7))
