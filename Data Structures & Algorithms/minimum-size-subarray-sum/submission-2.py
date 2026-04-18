class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        res = float('inf')

        subarray_sum = 0

        l = 0

        for r in range(len(nums)):
            subarray_sum += nums[r]

            while(subarray_sum >= target):
                res = min(res, r - l + 1)
                subarray_sum -= nums[l]
                l += 1
        
        if(res == float('inf')):
            res = 0
        
        return res
