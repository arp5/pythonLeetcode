class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        for i in range(n//2):
            for j in range(m):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j],matrix[i][j]
        print(matrix)
        for i in range(n):
            for j in range(i+1,m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix