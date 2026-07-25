class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_hp = []

        for num in nums:
            if(len(min_hp) < k):
                heapq.heappush(min_hp, (num))
            elif(num > min_hp[0]):
                heapq.heappop(min_hp)
                heapq.heappush(min_hp, num)
        
        return min_hp[0]