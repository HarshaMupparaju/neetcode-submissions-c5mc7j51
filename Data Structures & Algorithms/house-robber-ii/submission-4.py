class Solution:
    def rob(self, nums: List[int]) -> int:
            

        def rob_1(nums_arr: List[int]) -> int:
            if(len(nums) == 1):
                return nums[0]

            n = len(nums_arr)
            dp = [0] * (n + 2)
            # dp[n + 1] = 0
            # dp[n] = 0

            for i in range(n - 1, -1 , -1):
                dp[i] = max(nums_arr[i] + dp[i + 2], dp[i + 1])
            
            return dp[0]

        return max(rob_1(nums[:-1]), rob_1(nums[1:]))