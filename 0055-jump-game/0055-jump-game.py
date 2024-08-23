class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[-1] = True
        for i in reversed(range(n-1)):
            for j in range(i+1,min(i+nums[i]+1,n)):
                if dp[j]:
                    dp[i] = True
                    break
        #print(dp)
        return dp[0]