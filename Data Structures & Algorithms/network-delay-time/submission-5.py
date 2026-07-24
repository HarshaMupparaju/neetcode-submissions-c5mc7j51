class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = {i: [] for i in range(n + 1)} #0 - n inclusive

        for time in times:
            ui, vi, ti = time
            adj_list[ui].append([vi, ti])


        #We run dijkstras
        hp = []

        #Add the first node
        heapq.heappush(hp, (0, k))
        vis = set()

        res =  0
        while(hp):
            top = heapq.heappop(hp)
            time, node = top[0], top[1]

            if(node in vis):
                continue
            
            vis.add(node)
            res = time

            for nei, t in adj_list[node]:
                heapq.heappush(hp, (time + t, nei))
            

        #Check if number of nodes visited == n 
        if(len(vis) != n):
            res = -1
        
        return res