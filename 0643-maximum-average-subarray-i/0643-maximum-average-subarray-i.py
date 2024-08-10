class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cursum,maxsum = 0,-float('inf')
        for r in range(k):
            cursum+=nums[r]
        maxsum = max(maxsum,cursum)
        l = 0
        for r in range(k,n):
            cursum+=nums[r]
            cursum-=nums[l]
            l+=1
            maxsum = max(maxsum,cursum)
        return maxsum/k
