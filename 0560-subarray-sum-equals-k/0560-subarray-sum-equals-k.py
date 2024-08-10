class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixmap = {}
        prefixmap[0] = 1
        cur_sum,count = 0,0
        for num in nums:
            cur_sum+=num
            diff = cur_sum-k
            count+=prefixmap.get(diff,0)
            prefixmap[cur_sum]=1+prefixmap.get(cur_sum,0)
        return count