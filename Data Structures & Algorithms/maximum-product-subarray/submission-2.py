class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        cur_min, cur_max = 1, 1

        for num in nums:
            if(num == 0):
                cur_min, cur_max = 1, 1
                continue
            temp = num * cur_min
            cur_min = min(num * cur_min, num * cur_max, num)
            cur_max = max(temp, num * cur_max, num)
        
            res = max(res, cur_max)
        
        return res