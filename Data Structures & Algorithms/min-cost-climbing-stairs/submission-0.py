class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [-1] * n

        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for i in range(n - 3, -1, -1):
            dp[i] = min(cost[i] + dp[i + 1], cost[i] + dp[i + 2])

        return min(dp[0], dp[1])