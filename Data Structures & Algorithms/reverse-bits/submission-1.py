class Solution:
    def reverseBits(self, n: int) -> int:
        temp = 0

        idx = 31
        while(n > 0):
            if(n & 1 == 1):
                temp = (temp | (1 << idx))
            
            n = n >> 1
            idx -= 1
        
        return temp
