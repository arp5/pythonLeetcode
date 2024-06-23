class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        print(candidates)
        def bt(index,cur_sum,cur_comb):
            if cur_sum == target:
                print(cur_comb)
                ans.append(cur_comb[:])
                return
            if index>=len(candidates) or cur_sum>target:
                return
            cur_comb.append(candidates[index])
            cur_sum+=candidates[index]
            bt(index+1,cur_sum,cur_comb)
            cur_sum-=candidates[index]
            cur_comb.pop()
            while index+1<len(candidates) and candidates[index]==candidates[index+1]:
                index+=1
            bt(index+1,cur_sum,cur_comb)
        bt(0,0,[])
        return ans
            