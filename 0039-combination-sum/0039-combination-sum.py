class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def combSum(index,cur_sum, cur_comb):
            if cur_sum == target:
                ans.append(cur_comb[:])
                return
            if index>=len(candidates) or cur_sum>target:
                return
            cur_comb.append(candidates[index])
            cur_sum+=candidates[index]
            combSum(index,cur_sum,cur_comb)
            cur_sum-=candidates[index]
            cur_comb.pop()
            combSum(index+1,cur_sum,cur_comb)
        combSum(0,0,[])
        return ans

            