class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for i in range(k + 1):
            temp = prices.copy()
            print(temp)
            for u, v, p in flights:
                if(prices[u] + p < temp[v]):
                    temp[v] = prices[u] + p

            prices = temp
        
        print(temp)
        res = prices[dst]

        if(res == float('inf')):
            res = -1
        
        return res