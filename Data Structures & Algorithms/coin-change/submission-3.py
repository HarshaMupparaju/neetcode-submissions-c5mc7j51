class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(cur_amount: int):
            if(cur_amount in memo):
                return memo[cur_amount]
            if(cur_amount == 0):
                return 0
            
            if(cur_amount < 0):
                return float('inf')
            
            res = float('inf')
            for coin in coins:
                res = min(res, dfs(cur_amount - coin))
            
            if(res != float('inf')):
                res = 1 + res
            else:
                res = res

            
            memo[cur_amount] = res

            return res

        res = dfs(amount)

        if(res == float('inf')):
            res = -1

        return res