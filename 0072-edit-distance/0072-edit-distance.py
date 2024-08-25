class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        dp = [[float('inf') for j in range(m+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][m] = n-i
        for j in range(m+1):
            dp[n][j] = m-j
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1+min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
        print(dp)
        return dp[0][0]