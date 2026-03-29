class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]
        
        if(n == 2):
            return max(nums)
        dp = [-1] * n

        #Base case
        dp[-1] = nums[-1]
        dp[-2] = max(nums[-2], nums[-1])

        for i in range(n - 3, -1, -1):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        return max(dp[0], dp[1])