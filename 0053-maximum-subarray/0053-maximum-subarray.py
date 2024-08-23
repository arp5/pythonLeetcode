class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum,maxsum = -float('inf'), -float('inf')
        for num in nums:
            cursum = max(num,cursum+num)
            maxsum = max(maxsum,cursum)
        return maxsum