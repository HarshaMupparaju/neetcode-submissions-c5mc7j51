class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        start = 1
        end = max(piles)

        def possible(k) -> bool:
            num_hrs = 0

            for i in range(len(piles)):
                num_hrs += math.ceil(piles[i] / k)
        
            if(num_hrs <= h):
                res = True
            else:
                res = False
            
            return res

        res = start
        while(start <= end):

            mid = (start + end) // 2

            if(possible(mid)):
                end = mid - 1
                res = mid
            else:
                start = mid + 1
        
        return res