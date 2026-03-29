class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def num_coins(coins: List[int], amount: int, dp: List[int]):
            
            if(dp[amount] != -1):
                return dp[amount]

            # if(amount == 0):
            #     return 0
            

            min_coins = float('inf')

            for coin in coins:
                if(coin <= amount):
                    # flag = 1
                    num_coins(coins, amount - coin, dp)
                    temp = dp[amount - coin]
                    if(temp != float('inf')):
                        min_coins = min(min_coins, 1 + temp)
            
            dp[amount] = min_coins
            return

        dp = [-1] * (amount + 1)
        dp[0] = 0

        num_coins(coins, amount, dp)
        
        res = dp[-1]

        if(res == float('inf')):
            return -1

        return res