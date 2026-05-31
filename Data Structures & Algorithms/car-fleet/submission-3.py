class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        position_time = [] #(position, time)

        for i in range(len(position)):
            position_time.append((position[i], (target - position[i]) / speed[i]))
        

        position_time.sort(key=lambda x: x[0], reverse = True)

        res = 1
        i = 1
        cur_max = position_time[0][1]

        while(i < len(position_time)):
            if(position_time[i][1] > cur_max):
                print(i)
                res += 1
            cur_max = max(cur_max, position_time[i][1])
            i += 1
            
            
        return res
