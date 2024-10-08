class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if text1[i]==text2[j]:
                    dp[i][j] = 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0] 