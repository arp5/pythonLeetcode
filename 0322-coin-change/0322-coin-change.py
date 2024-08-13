class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # self.coins = float('inf')
        # def cc(cursum,curset,i):
        #     if cursum==amount:
        #         self.coins = min(self.coins,len(curset))
        #         return
        #     if i==len(coins) or cursum>amount:
        #         return
        #     curset.append(coins[i])
        #     cc(cursum+coins[i],curset,i)
        #     cc(cursum+coins[i],curset,i+1)
        #     curset.pop()
        #     cc(cursum,curset,i+1)
        # cc(0,[],0)
        # return self.coins if self.coins!=float('inf') else -1
        dp = [amount+1]*(amount+1)
        dp[-1]=0
        for i in reversed(range(amount+1)):
            if dp[i]!=amount+1:
                for c in coins:
                    if i-c>=0:
                        dp[i-c]=min(1+dp[i],dp[i-c])
        print(dp)
        return dp[0] if dp[0]!=amount+1 else -1
            