class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj_list = {i: [] for i in range(len(points))}
        vis = set()

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)
                adj_list[i].append([dist, j])
                adj_list[j].append([dist, i])
        
        hp = []
        res = 0

        heapq.heappush(hp, [0, 0, -1])

        while(hp):
            if(len(vis) == len(points)):
                return res
            w1, n1, p1 = heapq.heappop(hp)

            if(n1 in vis):
                continue
            
            vis.add(n1)
            res += w1

            for w2, n2 in adj_list[n1]:
                # if(n2 not in vis):
                heapq.heappush(hp, [w2, n2, n1])

        return res