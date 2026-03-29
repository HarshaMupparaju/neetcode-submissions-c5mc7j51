class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        res.append(0)
        if(n == 0):
            return res
        res.append(1)

        count = 0
        for i in range(2, n + 1):
            if(count == 0):
                count = i
            
            res.append(res[-count] + 1)
            count -= 1
        
        return res