class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n,total= len(nums),sum(nums)
        self.ans = False
        @lru_cache(maxsize=None)
        def rec(index,cur_sum):
            #base
            #print(index,cur_sum)
            if cur_sum==total-cur_sum:
                #self.ans = True
                return True
            if index>=n or cur_sum>total-cur_sum:
                return False
            #cur_sum+=nums[index]
            #cur_comb.append(nums[index])
            return rec(index+1,cur_sum+nums[index]) or rec(index+1,cur_sum)
            #cur_comb.pop()
            #cur_sum-=nums[index]
            #rec(index+1,cur_sum)
        return rec(0,0)
        #return self.ans