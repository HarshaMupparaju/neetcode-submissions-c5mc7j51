class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []

        for num in nums:
            heapq.heappush(hp, -num)
        
        for i in range(k - 1):
            heapq.heappop(hp)
        
        return -1 * heapq.heappop(hp)