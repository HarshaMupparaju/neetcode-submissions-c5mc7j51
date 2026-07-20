class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dfs(i: int) -> int:
            if(i in memo):
                return memo[i]
            if(i >= len(s)):
                return 1
            
            if(s[i] == '0'):
                return 0
            
            one = dfs(i + 1)
            
            two = 0
            if(i + 2 <= len(s) and int(s[i: i + 2]) < 27):
                two = dfs(i + 2)

            # print(f'{i}: {one + two}')
            memo[i] = one + two
            return one + two

        res = dfs(0)

        return res