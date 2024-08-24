class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1), len(text2)
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    if i>=1 and j>=1:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = 1
                else:
                    if i==0:
                        dp[i][j] = dp[i][j-1]
                    elif j==0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
