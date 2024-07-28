class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        matrixm = {}
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if j-i not in matrixm:
                    matrixm[j-i] = matrix[i][j]
                else:
                    if matrix[i][j] != matrixm[j-i]:
                        return False
        return True