class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if(sum(gas) < sum(cost)):
            return -1
        
        total = 0
        res = 0
        for i in range(len(gas)):
            if(total < 0):
                total = 0
                res = i
            
            total += gas[i] - cost[i]
        
        return res

        #Brute Force
        # def dfs(i: int, cur_gas: int, num_stations: int) -> bool:
        #     if(cur_gas < 0):
        #         return False

        #     if(num_stations == len(gas)):
        #         return True
            
        #     if((i, cur_gas, num_stations) in dp):
        #         return dp[(i, cur_gas, num_stations)]

        #     res = dfs(i + 1, cur_gas + gas[i % len(gas)] - cost[i % len(gas)], num_stations + 1)
        #     dp[(i, cur_gas, num_stations)] = res
        #     return res

        # for i, g in enumerate(gas):
        #     if(dfs(i, 0, 0)): #idx, cur_gas, number of stations
        #         return i
        
        # return -1
