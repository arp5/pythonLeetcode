class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        def bt(i,cur_comb):
            if i>=len(nums):
                if cur_comb not in ans:
                    ans.append(cur_comb[:])
                #ans.add(tuple(cur_comb[:]))
                return
            cur_comb.append(nums[i])
            bt(i+1,cur_comb)
            cur_comb.pop()
            bt(i+1, cur_comb)
        bt(0,[])
        return ans