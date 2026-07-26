class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cur_capacity = capacity
        min_hp = []
        trips.sort(key = lambda l: l[1])
        print(trips)
        for i in range(len(trips)):
            num_passengers = trips[i][0]
            from_i = trips[i][1]
            to_i = trips[i][2]

            while(len(min_hp) > 0 and min_hp[0][0] <= from_i):
                cur_capacity += heapq.heappop(min_hp)[1]

            if(cur_capacity < num_passengers):
                print(i)
                return False
            cur_capacity -= num_passengers
            heapq.heappush(min_hp, (to_i, num_passengers))
        
        return True