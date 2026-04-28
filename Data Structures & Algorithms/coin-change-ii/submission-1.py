class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        d = {} # Memo for 2 states

        def dfs(current_amount: int, i: int) -> int:
            if(current_amount == 0):
                return 1
            
            if(current_amount < 0):
                return 0
            
            if((current_amount, i) in d):
                return d[(current_amount, i)]
            
            res = 0
            # for j, coin in enumerate(coins[i:], i):
            #     res += dfs(current_amount - coin, j)
            
            for j in range(len(coins[i:])):
                res += dfs(current_amount - coins[i:][j], i + j)
            
            d[(current_amount, i)] = res
            return res

        res = dfs(amount, 0)

        return res