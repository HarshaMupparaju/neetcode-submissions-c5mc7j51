class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #Min head
        self.hp = []
        self.k = k

        for num in nums:
            heapq.heappush(self.hp, num)

    def add(self, val: int) -> int:

        heapq.heappush(self.hp, val)

        while(len(self.hp) > self.k):
            heapq.heappop(self.hp)
        
        return self.hp[0]
        
