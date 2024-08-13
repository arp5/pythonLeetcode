class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in reversed(range(n)):
            for j in reversed(range(i)):
                #print(i,j, nums[i], nums[j])
                if nums[j]<nums[i]:
                    dp[j] = max(dp[j], 1+dp[i])
        print(dp)
        return max(dp)