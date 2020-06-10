class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = []
        fib.extend([1, 1])
        j = 1
        i = 2
        # calculate fibonacci number greater than k
        while j < k:
            x = fib[i - 1] + fib[i - 2]
            fib.append(x)
            i += 1
            j = x
        count = 0
        for i in range(len(fib) - 1, -1, -1):
            print(fib[i], k)
            if fib[i] == k:
                count += 1
                break
            elif fib[i] < k:
                k = k - fib[i]
                count += 1
        return count
