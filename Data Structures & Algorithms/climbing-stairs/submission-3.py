class Solution:
    def climbStairs(self, n: int) -> int:
        if(n == 1):
            return 1
        dp = [0] * (n)
        dp[n - 1] = 1
        dp[n - 2] = 2

        for i in range(n - 3, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        
        return dp[0]

        # #Top Down; TC: O(n); SC: O(n)
        # memo = {}
        # def dfs(position: int) -> int:
        #     if(position in memo):
        #         return memo[position]

        #     if(position == n):
        #         return 1
            
        #     if(position > n):
        #         return 0
            
        #     one = dfs(position + 1) #1 step
        #     two = dfs(position + 2) #2 step

        #     memo[position] = one + two
        #     return one + two

        # res = dfs(0)

        # return res