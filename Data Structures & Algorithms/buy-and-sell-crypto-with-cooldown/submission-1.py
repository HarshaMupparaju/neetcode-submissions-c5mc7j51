class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         
        n = len(prices)

        dp = {}

        def dfs(day: int, inventory: bool) -> int:
            if(day >= n):
                return 0
            
            if((day, inventory) in dp):
                return dp[(day, inventory)]

            if(inventory):
                sell_today = prices[day] + dfs(day + 2 , False)
                cd_today = dfs(day + 1, inventory)

                res = max(sell_today, cd_today)

            else:
                buy_today = - prices[day] + dfs(day + 1, True)
                cd_today = dfs(day + 1, inventory)
                res = max(buy_today, cd_today)
            
            dp[(day, inventory)] = res

            return res


        res = dfs(0, False)

        return res
