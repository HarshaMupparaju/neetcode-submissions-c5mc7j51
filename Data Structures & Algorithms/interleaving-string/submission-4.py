class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if(len(s1) + len(s2) != len(s3)):
            return False

        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if(i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]):
                    dp[i][j] = True
                
                if(j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]):
                    dp[i][j] = True
                
                # dp[i][j] = False



        return dp[0][0]







        # memo = {}

        # def dfs(i: int, j: int) -> bool:
            
        #     if((i, j) in memo):
        #         return memo[(i, j)]

        #     if(i + j >= len(s3)):
        #         memo[(i, j)] = True
        #         return True
            
        #     if(i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j)):
        #         memo[(i, j)] = True
        #         return True
            
        #     if(j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1)):
        #         memo[(i, j)] = True
        #         return True
            
        #     memo[(i, j)] = False
        #     return False

        # if((len(s3) < len(s1) + len(s2)) or (len(s3) > len(s1) + len(s2))):
        #     return False

        # res = dfs(0, 0)

        # return res