class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        A = []

        for ky in d:
            heapq.heappush(A, (-d[ky], ky))
        
        res = []

        for i in range(k):
            res.append(A[0][1])
            heapq.heappop(A)[0]
        
        return res