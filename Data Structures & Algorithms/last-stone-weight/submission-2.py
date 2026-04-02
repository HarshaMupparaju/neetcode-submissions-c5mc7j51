class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []

        for i in range(len(stones)):
            heapq.heappush(hp, -stones[i])

        while(len(hp) > 1):
            x = -heapq.heappop(hp)
            y = -heapq.heappop(hp)

            if(x != y):
                heapq.heappush(hp, -abs(y - x))
        
        if(len(hp) == 0):
            res = 0
        else:
            res = -hp[0]
        
        return res