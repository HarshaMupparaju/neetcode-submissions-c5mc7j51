class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n == 0):
            return 1
        
        if(n > 0):
            sign = 1
        else:
            sign = -1
            n = n * -1
        
        res = 1
        
        for i in range(n):
            res = res * x
        
        if(sign == -1):
            res = 1 / res
        
        return res