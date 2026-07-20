class Solution:
    def rob(self, nums: List[int]) -> int:
        #Top-Down; TC: O(n * sum(nums)); TC: O(n * sum(nums))
        n = len(nums)
        memo = {}

        def dfs(i: int) -> int:
            if(i in memo):
                return memo[i]

            if(i >= n):
                return 0
            
            #hit
            hit = nums[i] + dfs(i + 2)

            #don't hit
            dont_hit = dfs(i + 1)

            memo[i] = max(hit, dont_hit)
            return max(hit, dont_hit)

        res = dfs(0)

        return res