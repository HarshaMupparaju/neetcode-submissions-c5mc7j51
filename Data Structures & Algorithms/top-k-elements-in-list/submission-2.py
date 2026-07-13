class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} #count, num

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        hp = []

        for key in d:
            heapq.heappush(hp, (-d[key], key))
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(hp)[1])
        
        return res

