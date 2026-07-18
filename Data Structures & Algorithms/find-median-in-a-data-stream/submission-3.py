class MedianFinder:

    def __init__(self):
        self.lesser_hp = [] #max heap
        self.greater_hp = [] #min heap
        self.elements = 0


    def addNum(self, num: int) -> None:
        self.elements += 1
        if(len(self.lesser_hp) == 0):
            heapq.heappush(self.lesser_hp, -num)
            return 
        
        if(-self.lesser_hp[0] < num):
            heapq.heappush(self.greater_hp, num)
        else:
            heapq.heappush(self.lesser_hp, -num)
        
        while(len(self.lesser_hp) - len(self.greater_hp) > 1):
            top = heapq.heappop(self.lesser_hp)
            heapq.heappush(self.greater_hp, -top)
        
        while(len(self.greater_hp) - len(self.lesser_hp) > 1):
            top = heapq.heappop(self.greater_hp)
            heapq.heappush(self.lesser_hp, -top)
        
        return

    def findMedian(self) -> float:
        print(self.elements)
        print(self.lesser_hp)
        print(self.greater_hp)

        if(self.elements % 2 == 0):
            res = (-self.lesser_hp[0] + (self.greater_hp[0])) / 2
        else:
            if(len(self.lesser_hp) > len(self.greater_hp)):
                res = -self.lesser_hp[0]
            else:
                res = self.greater_hp[0]
        
        return res
        
        