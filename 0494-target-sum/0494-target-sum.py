class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.count = 0
        ans = []
        dp = {}
        #@lru_cache(maxsize=None)
        def rec(index,cur_sum):
            #base
            #print(index,cur_sum, cur_comb)
            if (index,cur_sum) in dp:
                return dp[(index,cur_sum)]
            if cur_sum==target and index==len(nums):
                #self.count+=1
                #ans.append(cur_comb[:])
                return 1
            if index>=len(nums):
                return 0
            #cur_sum+=nums[index]
            #cur_comb.append(nums[index])
            #rec(index+1,cur_sum)
            #cur_comb.pop()
            #cur_sum-=(2*nums[index])
            #cur_comb.append(-nums[index])
            #rec(index+1,cur_sum)
            dp[(index,cur_sum)] =  rec(index+1,cur_sum+nums[index]) + rec(index+1,cur_sum-nums[index])
            return dp[(index,cur_sum)]
        return rec(0,0)
        #print(ans)
        #return self.count