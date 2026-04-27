class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Memoization solution
        n = len(nums)

        s = sum(nums)

        if(s % 2 == 1):
            return False # Odd sum can't be partitioned
        
        target = s // 2

        memo = {}

        def dfs(i: int, t: int) -> bool:
            if(t == 0):
                return True
            elif(t < 0 ):
                return False
            
            if(i >= n):
                return False

            if((i, t) in memo):
                return memo[(i, t)]
            
            #Take the current element
            take = dfs(i + 1, t - nums[i])

            #Don't take the current element
            skip = dfs(i + 1, t)
            
            res = take or skip

            memo[(i, t)] = res

            return res

        res = dfs(0, target)

        return res