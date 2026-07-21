class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #TC: O(n); SC: O(1)
        res = max(nums)

        cur_min = 1
        cur_max = 1

        for num in nums:
            if(num == 0):
                cur_min = 1
                cur_max = 1
            
            temp = cur_max
            cur_max = max( num * cur_max, num * cur_min, num)
            cur_min = min(num * temp, num * cur_min, num)

            res = max(res, cur_max)

        return res