class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = set()
        dp.add(0)
        total = sum(nums)
        if total%2:
            return False
        target = total//2
        for i in range(len(nums)-1,-1,-1):
            nextdp = set()
            for ts in dp:
                if ts+nums[i] == target:
                    return True
                nextdp.add(ts+nums[i])
                nextdp.add(ts)
            dp = nextdp
        return True if target in dp else False
            
                