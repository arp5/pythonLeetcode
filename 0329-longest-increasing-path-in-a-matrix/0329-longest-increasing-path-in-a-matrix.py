class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        n,m = len(matrix), len(matrix[0])
        def dfs(i,j, pval):
            if i<0 or i>=n or j<0 or j>=m or matrix[i][j]<=pval:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            res = 1
            res = max(res, 1+dfs(i-1,j,matrix[i][j]))
            res = max(res, 1+dfs(i+1,j,matrix[i][j]))
            res = max(res, 1+dfs(i,j-1,matrix[i][j]))
            res = max(res, 1+dfs(i,j+1,matrix[i][j]))
            dp[(i,j)] = res
            return res
        for i in range(n):
            for j in range(m):
                dfs(i,j,-1)
        return max(dp.values())