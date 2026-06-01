class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        #Base case last column, word2 is ""
        temp = n
        for i in range(n):
            dp[i][m] = temp
            temp -= 1
        
        #Base case last row, word1 is ""
        temp = m
        for i in range(m):
            dp[n][i] = temp
            temp -= 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if(word1[i] == word2[j]):
                    #No op
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]) # min(insert, delete, replace)
        
        return dp[0][0]

        # n = len(word1)
        # m = len(word2)

        # memo = {}

        # ##Brute Force: O(3^n)
        # #Top Down: O(n * m)
        # def dfs(i: int, j: int) -> int:
        #     if(i == n and j == m):
        #         memo[(i, j)] = 0
        #         return 0
        #     if(i == n):
        #         memo[(i, j)] = (m - j)
        #         return (m - j)
        #     if(j == m):
        #         memo[(i, j)] = (n - i)
        #         return (n - i)
            
        #     if((i, j) in memo):
        #         return memo[(i, j)]
            
        #     res = 0

        #     if(word1[i] == word2[j]):
        #         res = dfs(i + 1, j + 1)
        #     else:
        #         #Insert
        #         res1 = dfs(i, j + 1)
        #         #Delete
        #         res2 = dfs(i + 1, j)
        #         #Replace
        #         res3 = dfs(i + 1, j + 1)

        #         res = 1 + min(res1, res2, res3)
            
        #     memo[(i, j)] = res
        #     return res

        # res = dfs(0, 0)

        # return res