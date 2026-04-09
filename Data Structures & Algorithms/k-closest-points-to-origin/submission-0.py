class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        hp = []

        for i in range(len(points)):
            xi = points[i][0]
            yi = points[i][1]

            dist = math.sqrt(xi ** 2 + yi ** 2)
            heapq.heappush(hp, (dist, points[i]))
        
        for i in range(k):
            res.append(heapq.heappop(hp)[1])
        
        return res