class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(o: int, c: int, s: str) -> None:
            if(o == n and  c == n):
                res.append(s)
                return
            elif(o + c >= 2*n):
                return
            
            #add (
            dfs(o + 1, c, s + '(')

            #add )
            if(c < o):
                dfs(o, c + 1, s + ')')

        
        dfs(0, 0, '')

        return res

            
        
