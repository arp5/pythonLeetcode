class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        isCol = False
        for i in range(n):
            if matrix[i][0]==0:
                isCol = True
            for j in range(1,m):
                if matrix[i][j] == 0:
                    matrix[i][0] =0
                    matrix[0][j] =0
        
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(1,m):
                    matrix[i][j] = 0
        
        for j in range(1,m):
            if matrix[0][j] == 0:
                for i in range(1,n):
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if isCol:
            for i in range(n):
                matrix[i][0] = 0