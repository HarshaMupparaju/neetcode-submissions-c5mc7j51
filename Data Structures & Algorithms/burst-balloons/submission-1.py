class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        memo = {}
        ##O(n! x n)
        def dfs(temp: List[int]) -> int:
            if(len(temp) == 0):
                memo[tuple(temp)] = 0 
                return 0
            
            if(tuple(temp) in memo):
                return memo[tuple(temp)]
            
            res = float('-inf')
            for i in range(len(temp)):
                temp_copy = temp.copy()
                temp_copy.pop(i)
                if(i == 0 and i + 1 == len(temp)):
                    res = max(res, 1 * temp[i] * 1 + dfs(temp_copy))
                elif(i == 0):
                    res = max(res, 1 * temp[i] * temp[i + 1] + dfs(temp_copy))
                elif(i + 1 == len(temp)):
                    res = max(res, temp[i - 1] * temp[i] * 1 + dfs(temp_copy))
                else:
                    res = max(res, temp[i - 1] * temp[i] * temp[i + 1] + dfs(temp_copy))
            
            memo[tuple(temp)] = res
            return res


        res = dfs(nums)

        return res