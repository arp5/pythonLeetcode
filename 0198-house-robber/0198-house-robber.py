class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for x in range(n)]
        dp[0] = nums[0]
        if n==1:
            return nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            print(i)
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]