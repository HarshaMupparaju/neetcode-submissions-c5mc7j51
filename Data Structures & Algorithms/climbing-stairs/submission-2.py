class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(position: int) -> int:
            if(position in memo):
                return memo[position]

            if(position == n):
                return 1
            
            if(position > n):
                return 0
            
            one = dfs(position + 1) #1 step
            two = dfs(position + 2) #2 step

            memo[position] = one + two
            return one + two

        res = dfs(0)

        return res