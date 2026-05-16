class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        d = {} # Memo

        def dfs(idx: int, target: int) -> int:
            if((idx, target) in d):
                return d[(idx, target)]
            
            if(idx == n and target == 0):
                d[(idx, target)] = 1
                return d[(idx, target)]
            
            if(idx >= n):
                d[(idx, target)] = 0
                return d[(idx, target)]
            
            left = dfs(idx + 1, target - nums[idx])
            right = dfs(idx + 1, target + nums[idx])

            d[(idx, target)] = left + right
        
            return d[(idx, target)]

        print(d)
        res = dfs(0, target)

        return res