class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def perm(index,cur_comb):
            #base?
            print(index, cur_comb)
            if len(cur_comb)==len(nums):
                ans.append(cur_comb[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in cur_comb:
                    cur_comb.append(nums[i])
                    perm(i,cur_comb)
                    cur_comb.pop()
        perm(0,[])
        return ans