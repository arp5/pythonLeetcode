class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def bt(i,cur_comb):
            if i>=len(nums):
                ans.append(cur_comb[:])
                return
            cur_comb.append(nums[i])
            bt(i+1,cur_comb)
            cur_comb.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            bt(i+1,cur_comb)
        bt(0,[])
        return ans