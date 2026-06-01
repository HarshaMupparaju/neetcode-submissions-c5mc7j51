class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #O(n^2 * n) TC and O(n^2) SC
        #Pad nums
        nums = [1] + nums + [1]

        memo = {}

        def dfs(l: int, r: int) -> int:
            if(l > r):
                return 0
            
            if((l, r) in memo):
                return memo[(l, r)]
            
            res = float('-inf')
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1)
                coins += dfs(i + 1, r)
                res = max(res, coins)
            
            memo[(l, r)] = res
            return res

        res = dfs(1, len(nums) - 2)
        return res

        # memo = {}
        # ##Brute Force: O(n! x n)
        # ##Simple Memoization: O(2^n x n)
        # def dfs(temp: List[int]) -> int:
        #     if(len(temp) == 0):
        #         memo[tuple(temp)] = 0 
        #         return 0
            
        #     if(tuple(temp) in memo):
        #         return memo[tuple(temp)]
            
        #     res = float('-inf')
        #     for i in range(len(temp)):
        #         temp_copy = temp.copy()
        #         temp_copy.pop(i)
        #         if(i == 0 and i + 1 == len(temp)):
        #             res = max(res, 1 * temp[i] * 1 + dfs(temp_copy))
        #         elif(i == 0):
        #             res = max(res, 1 * temp[i] * temp[i + 1] + dfs(temp_copy))
        #         elif(i + 1 == len(temp)):
        #             res = max(res, temp[i - 1] * temp[i] * 1 + dfs(temp_copy))
        #         else:
        #             res = max(res, temp[i - 1] * temp[i] * temp[i + 1] + dfs(temp_copy))
            
        #     memo[tuple(temp)] = res
        #     return res


        # res = dfs(nums)

        # return res