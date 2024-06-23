class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(i,cur_comb):
            if i>=len(nums):
                ans.append(cur_comb[:])
                return
            cur_comb.append(nums[i])
            bt(i+1,cur_comb)
            cur_comb.pop()
            bt(i+1,cur_comb)
        bt(0,[])
        return ans