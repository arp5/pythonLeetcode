class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.count = 0
        combs = []
        dp = {}
        #@lru_cache(maxsize=None)
        def rec(index,cur_sum):
            #print(index,cur_sum,cur_comb)
            if (index,cur_sum) in dp:
                return dp[(index,cur_sum)]
            if cur_sum == amount:
                #self.count+=1
                #combs.append(cur_comb[:])
                return 1
            if index>=len(coins) or cur_sum>amount:
                return 0
            #cur_comb.append(coins[index])
            #cur_sum+=coins[index]
            #rec(index,cur_sum, cur_comb)
            #cur_sum-=coins[index]
            #cur_comb.pop()
            #rec(index+1,cur_sum, cur_comb)
            dp[(index,cur_sum)] = rec(index,cur_sum+coins[index])+rec(index+1,cur_sum)
            return dp[(index,cur_sum)]
        n = len(coins)
        return rec(0,0)
        #print(combs)
        #return self.count