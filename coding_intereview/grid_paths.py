from math import factorial


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def uniquePaths(self ,A, B):
        A -= 1
        B -= 1

        return factorial(A + B) / (factorial(A) * factorial(B))

print(Solution().uniquePaths(3,3))