class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hp = []

        time = [float('inf')] * (n+1)

        time[0] = 0

        #Make adj list
        adj_list = {i:[] for i in range(n + 1)}

        for t in times:
            adj_list[t[0]].append([t[1], t[2]])

        heapq.heappush(hp, [0, k]) # Push the source node, [time, node]

        while(len(hp) > 0):
            top = heapq.heappop(hp)
            if(top[0] < time[top[1]]):
                time[top[1]] = top[0]
            else:
                continue
            
            for nei in adj_list[top[1]]:
                print(nei)
                heapq.heappush(hp, [top[0] + nei[1], nei[0]])
        
        res = -1
        
        for i in range(len(time)):
            res = max(res, time[i])
        
        if(res == float('inf')):
            res = -1

        return res