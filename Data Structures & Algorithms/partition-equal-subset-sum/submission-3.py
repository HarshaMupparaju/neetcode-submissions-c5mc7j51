class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Bottom Up
        n = len(nums)
        s = sum(nums)

        dp = [False] * n

        if(s % 2 == 1):
            return False #An odd sum array can't be split into 2

        target = s // 2

        s = set()
        s.add(0)

        for i in range(n - 1, -1, -1):
            temp = s.copy()
            for ele in temp:
                if(ele + nums[i] not in s):
                    s.add(ele + nums[i])
            
            if(target in s):
                dp[i] = True
            else:
                dp[i] = False
            
        print(dp)
        return dp[0]