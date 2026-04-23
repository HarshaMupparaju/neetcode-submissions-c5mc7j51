class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(x == 0):
            return 0

        if(n >= 0):
            sign = 1
        else:
            sign = -1
            n = n * -1

        def dfs(n: int) -> float:
            if(n == 0):
                return 1
            
            temp = dfs(n // 2)
            if(n % 2 == 1):
                res = temp * temp * x
            else:
                res = temp * temp
            
            return res

        res = dfs(n)

        if(sign == -1):
            res = 1 / res

        return res