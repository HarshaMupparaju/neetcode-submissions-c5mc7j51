class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = {} #Undirected Graph

        for point in points:
            adj_list[tuple(point)] = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                point1 = points[i]
                point2 = points[j]

                dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

                adj_list[tuple(point1)].append([point2[0], point2[1], dist])

                adj_list[tuple(point2)].append([point1[0], point1[1], dist])
        
        vis = set()
        res = 0

        pq = [] #Min Heap
        heapq.heappush(pq, (0, points[0][0], points[0][1])) #(u, v, 0)

        while(len(pq) != 0):
            d, u, v = heapq.heappop(pq)

            if((u, v) in vis):
                continue
            
            vis.add((u, v))
            res += d

            for nei in adj_list[(u, v)]:
                if((nei[0], nei[1]) not in vis):
                    heapq.heappush(pq, (nei[2], nei[0], nei[1]))

        return res