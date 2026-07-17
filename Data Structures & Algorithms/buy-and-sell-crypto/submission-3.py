class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #TC: O(n) and S: O(1)
        l = 0
        r = 1
        res = 0
        while(r < len(prices)):

            if(prices[l] > prices[r]):
                l = r
            else:
                res = max(res, prices[r] - prices[l])
            
            r += 1
        
        return res


        # #TC: O(n) and SC: O(n)
        # suffix_arr = []

        # cur_max = 0
        # for i in range(len(prices) - 1, -1, -1):
        #     suffix_arr.append(cur_max)
        #     cur_max = max(cur_max, prices[i])
        
        # suffix_arr.reverse()

        # res = 0
        # for i in range(len(prices)):
        #     res = max(res, suffix_arr[i] - prices[i])
        
        # return res