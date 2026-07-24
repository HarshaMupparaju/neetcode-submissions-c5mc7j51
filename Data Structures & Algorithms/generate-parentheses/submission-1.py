class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recurse(o: int, c: int, cur_str: ''):
            if(o > n or c > n):
                return
            
            if(o == n and c == n):
                res.append(cur_str)
                return
            
            #Add open 
            recurse(o + 1, c, cur_str + '(')

            #Add close
            if(c < o ):
                recurse(o, c + 1, cur_str + ')')
            
            return
            
        recurse(0, 0, '')

        return res