class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[-1] = 1


        for i in range(n - 1 - 1, -1, -1):
            cur_max = 1
            for j in range(n - 1, i , -1):
                if(nums[i] < nums[j]):
                    cur_max = max(cur_max, 1 + dp[j])
                # else:
                #     cur_max = max(cur_max, dp[j])
            
            dp[i] = cur_max

        print(dp)    
        return max(dp)


    