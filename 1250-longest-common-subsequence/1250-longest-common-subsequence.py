class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1), len(text2)
        max_len = 0
        dp = [[0 for y in range(m)] for x in range(n)]
        for i in range(n):
            for j in range(m):
                if text1[i]==text2[j]:
                    #print(i,j,dp[i-1][j-1])
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                max_len = max(max_len, dp[i][j])
        #print(dp)
        return max_len