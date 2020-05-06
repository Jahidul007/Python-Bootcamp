class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        if n == 1:
            return 0
        if n%2==0:

            count=self.integerReplacement(n / 2)+1;

        else:
            count=min(self.integerReplacement(n - 1), self.integerReplacement(n + 1))+1

        return count