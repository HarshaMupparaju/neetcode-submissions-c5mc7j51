class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        suffix_arr = []

        cur_max = 0
        for i in range(len(prices) - 1, -1, -1):
            suffix_arr.append(cur_max)
            cur_max = max(cur_max, prices[i])
        
        suffix_arr.reverse()

        res = 0
        for i in range(len(prices)):
            res = max(res, suffix_arr[i] - prices[i])
        
        return res