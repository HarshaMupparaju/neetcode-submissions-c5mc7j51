class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {} #Directed Graph

        for i in range(1, n + 1):
            adj_list[i] = []
        
        for edge in times:
            ui = edge[0]
            vi = edge[1]
            ti = edge[2]

            adj_list[ui].append((vi, ti))
        
        pq = [] # Minimum heap

        heapq.heappush(pq, (0, k)) #Starting node

        vis = set()

        nodes_reached = 0
        res = float('-inf')

        while(len(pq) > 0):
            top = heapq.heappop(pq)
            w_curr = top[0]
            node = top[1]

            if(node in vis):
                continue
            
            res = max(res, w_curr)
            vis.add(node)
            nodes_reached += 1

            for nei_w in adj_list[node]:
                nei = nei_w[0]
                w = nei_w[1]

                heapq.heappush(pq, (w_curr + w, nei))
        
        if(nodes_reached != n):
            return -1

        return res

            