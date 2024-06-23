class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod,min_prod = 1,1
        ans = -float('inf')
        for num in nums:
            prev_max = max_prod*num
            max_prod = max(max_prod*num, min_prod*num,num)
            min_prod = min(prev_max, min_prod*num, num)
            ans = max(max_prod,ans)
        return ans