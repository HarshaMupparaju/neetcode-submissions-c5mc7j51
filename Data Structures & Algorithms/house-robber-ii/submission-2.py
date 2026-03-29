class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if(n == 1):
            return nums[0]

        def house_robber_1(arr: List[int]) -> int:
            dp = [0] * len(arr)

            if(len(arr) == 1 or len(arr) == 2):
                return max(arr)

            #Base case
            dp[-1] = arr[-1]
            dp[-2] = max(arr[-2], arr[-1])

            for i in range(len(arr) -3, -1, -1):
                dp[i] = max(dp[i + 1], arr[i] + dp[i + 2])
            
            return max(dp[0], dp[1])
        
        return max(house_robber_1(nums[: n - 1]), house_robber_1(nums[1:]))