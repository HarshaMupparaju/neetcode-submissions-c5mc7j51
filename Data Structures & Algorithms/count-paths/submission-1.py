class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Bottom-Up
        res = 0
        dp = [[-1] * n for _ in range(m)]

        #Last col
        for i in range(m):
            dp[i][-1] = 1
        
        #Last row
        for i in range(n):
            dp[-1][i] = 1
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        
        return dp[0][0]