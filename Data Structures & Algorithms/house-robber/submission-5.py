class Solution:
    def rob(self, nums: List[int]) -> int:
        #Bottom-Up; TC: O(n); Sc: O(n)
        n = len(nums)
        dp = [0] * (n + 2)

        for i in range(n - 1, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])

        return dp[0]

        # #Top-Down; TC: O(n ); TC: O(n)
        # n = len(nums)
        # memo = {}

        # def dfs(i: int) -> int:
        #     if(i in memo):
        #         return memo[i]

        #     if(i >= n):
        #         return 0
            
        #     #hit
        #     hit = nums[i] + dfs(i + 2)

        #     #don't hit
        #     dont_hit = dfs(i + 1)

        #     memo[i] = max(hit, dont_hit)
        #     return max(hit, dont_hit)

        # res = dfs(0)

        # return res