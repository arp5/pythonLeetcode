class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum,max_sum = -float('inf'), -float('inf')
        for num in nums:
            cur_sum = max(num, cur_sum+num)
            max_sum = max(max_sum,cur_sum)
        return max_sum
