class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #TC: O(V + E + E log E); SC: O(V + E + V + V)
        n = len(points)
        adj_list = {i: [] for i in range(n)}

        #Make adj_list
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj_list[i].append([j, dist])
                adj_list[j].append([i, dist])

        #Initiate priority Queue
        hp = []
        heapq.heappush(hp, (0, 0)) #(dist, node)
        res = 0
        vis = set()

        #Run Dijkstra
        while(len(vis) < n):
            top = heapq.heappop(hp)

            if(top[1] in vis):
                continue

            vis.add(top[1])
            res += top[0]
            for nei in adj_list[top[1]]:
                heapq.heappush(hp, (nei[1], nei[0]))

        #Return
        return res