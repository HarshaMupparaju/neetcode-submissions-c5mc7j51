class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

        self.n = 0


    def addNum(self, num: int) -> None:
        if(self.n == 0):
            heapq.heappush(self.min_heap, num)
            self.n += 1
            return
        
        if(self.min_heap[0] <= num):
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
            

        #Rearrange
        while(abs(len(self.min_heap) - len(self.max_heap)) > 1):
            if(len(self.min_heap) > len(self.max_heap)):
                temp = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -temp)
            else:
                temp = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, temp)

        self.n += 1

        return

    def findMedian(self) -> float:
        if(self.n % 2 == 0):
            res = (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            if(len(self.min_heap) > len(self.max_heap)):
                res = float(self.min_heap[0])
            else:
                res = float(-self.max_heap[0])
        
        return res
        