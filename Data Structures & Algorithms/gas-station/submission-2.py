class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        temp = []

        for i in range(len(gas)):
            temp.append(gas[i] - cost[i])
        
        res = -1
        max_till_now = float('-inf')

        if(sum(temp) >= 0):
            #A solution exists
            for i in range(len(temp)):
                if(temp[i] >= 0):
                    cur = 0
                    j = i
                    count = 0
                    while(count < len(temp)):
                        cur += temp[j]
                        if(cur < 0):
                            break
                        j += 1
                        j = j % len(temp)
                        count += 1
                    
                    if(cur >= 0):
                        res = i
                        break


        return res