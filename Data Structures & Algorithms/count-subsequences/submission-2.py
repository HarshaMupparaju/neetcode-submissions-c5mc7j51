class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        n = len(s)
        m = len(t)

        dp = [[0] * (n+1) for _ in range(m + 1)]

        for i in range(n + 1): #Base case, empty string t
            dp[m][i] = 1

        for i in range(m - 1, -1, -1): #i is for t
            for j in range(n - 1, -1, -1): # j is for s
                if(t[i] == s[j]):
                    dp[i][j] = dp[i + 1][j + 1] + dp[i][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
        
        return dp[0][0]








        # memo = {}

        # ## O(2^n) - Recurse, no memoization
        # #O(n^2) where n is the length of the string
        # def dfs(temp: str, i: int) -> int:

        #     if((temp, i) in memo):
        #         return memo[(temp, i)]

        #     if(i == len(s)):
        #         if(temp == t):
        #             memo[(temp, i)] = 1
        #             return 1
        #         memo[(temp, i)] = 0
        #         return 0
            
        #     res1 = dfs(temp + s[i], i + 1) #Add the current character
        #     res2 = dfs(temp , i + 1) #We ignore the current character

        #     memo[(temp, i)] = res1 + res2

        #     return res1 + res2


        # res = dfs("", 0)

        # return res