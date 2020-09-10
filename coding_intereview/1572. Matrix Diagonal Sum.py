class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]  # elements from the primary diagonal
            total += mat[i][len(mat)-1-i]  # secondary diagonal
        if len(mat) % 2 == 0:
            return total
        return total - mat[len(mat)//2][len(mat)//2]
