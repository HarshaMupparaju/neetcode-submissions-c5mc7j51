class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i: int, j: int) -> bool:

            if(i == len(s) and j == len(p)):
                return True
            if(j == len(p)):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if(j + 1 < len(p) and p[j + 1] == '*'):
                res = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                res = dfs(i + 1, j + 1)
            else:
                res = False
        
            return res
            


        res = dfs(0, 0)

        return res