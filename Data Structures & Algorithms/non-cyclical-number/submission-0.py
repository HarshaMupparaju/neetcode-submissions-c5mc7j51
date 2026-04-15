class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        temp = n

        while(temp != 1):            
            s = 0

            while(temp > 0):
                rem = temp % 10
                temp = temp // 10

                s += rem ** 2
            
            if(s in d):
                return False
            else:
                d[s] = 1
            
            temp = s

        return True