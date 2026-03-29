class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_from_left = []
        current_lowest = prices[0]
        highest_from_right = []

        current_highest = prices[-1]




        for i in range(len(prices)):
            if(current_lowest > prices[i]):
                current_lowest = prices[i]
            
            lowest_from_left.append(current_lowest)
            
            if(current_highest < prices[len(prices) - 1 - i]):
                current_highest = prices[len(prices) - 1 - i]

            highest_from_right.append(current_highest)
        
        print(lowest_from_left)
        print(highest_from_right)

        highest_from_right.reverse()

        res = 0
        for i in range(len(lowest_from_left)):
            res = max(highest_from_right[i] - lowest_from_left[i], res)
        
        return res