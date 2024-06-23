class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def ss(index,cur_comb):
            if cur_comb not in ans:
                ans.append(cur_comb.copy())
            if index>=len(nums):
                return
            for i in range(index,len(nums)):
                if nums[i] not in cur_comb:
                    cur_comb.add(nums[i])
                    ss(index+1,cur_comb)
                    cur_comb.remove(nums[i])
        ss(0,set())
        return ans
            