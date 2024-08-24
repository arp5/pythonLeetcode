class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(index,cursum):
            if index==len(nums):
                return 1 if cursum==target else 0
            if (index,cursum) in dp:
                return dp[(index,cursum)]
            dp[(index,cursum)] = backtrack(index+1,cursum+nums[index])+backtrack(index+1,cursum-nums[index])
            return dp[(index,cursum)]
        return backtrack(0,0)