class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res = []

        temp = []

        for i in range(len(arr)):
            temp.append(arr[i] - x)
        
        if(temp[-1] <= 0):
            #whole arr is -ve
            i = 1
            while(i <= k):
                res.append(arr[-i])
                i += 1
        elif(temp[0] >= 0):
            #whole arr is +ve
            i = 0
            while(i < k):
                res.append(arr[i])
                i += 1
        else:
            i = 0
            while(temp[i] < 0):
                i += 1
    
            l = i - 1
            r = i
            j = 0
            while( l >= 0 and r < len(temp) and j < k):
                if(abs(temp[l]) <= abs(temp[r])):
                    res.append(arr[l])
                    l -= 1
                else:
                    res.append(arr[r])
                    r += 1
                j += 1
            
            if(len(res) != k):
                if(l < 0 ):
                    while(len(res) < k):
                        res.append(arr[r])
                        r += 1
                else:
                    while(len(res) < k):
                        res.append(arr[l])
                        l -= 1

        res.sort()

        return res