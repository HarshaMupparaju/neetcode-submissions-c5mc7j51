class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        def dfs(i: int, j: int) -> bool:
            
            if((i, j) in memo):
                return memo[(i, j)]

            if(i + j >= len(s3)):
                memo[(i, j)] = True
                return True
            
            if(i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j)):
                memo[(i, j)] = True
                return True
            
            if(j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1)):
                memo[(i, j)] = True
                return True
            
            memo[(i, j)] = False
            return False

        if((len(s3) < len(s1) + len(s2)) or (len(s3) > len(s1) + len(s2))):
            return False

        res = dfs(0, 0)

        return res