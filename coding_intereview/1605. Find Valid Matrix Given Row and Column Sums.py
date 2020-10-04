class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row = len(rowSum)
        col = len(colSum)
        
        mat = [[0] * col for i in range(row)]
        
        for i in range (row):
            for j in range (col):
                mat[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= mat[i][j]
                colSum[j] -= mat[i][j]
        return mat
