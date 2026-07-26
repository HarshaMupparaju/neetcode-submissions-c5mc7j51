class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #TC: O(n * log(n) + n * lon(n)); SC: O(n)
        max_hp = []

        for stone in stones:
            heapq.heappush(max_hp, -stone)
        
        while(len(max_hp) > 1):
            x = - heapq.heappop(max_hp)
            y = - heapq.heappop(max_hp)

            if(x != y):
                heapq.heappush(max_hp, - abs(x - y))

        if(len(max_hp) == 0):
            res = 0
        else:
            res = - heapq.heappop(max_hp)
        
        return res