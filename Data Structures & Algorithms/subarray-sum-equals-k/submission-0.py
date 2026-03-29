class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {}

        #Edge case init
        prefix_sum[0] = 1

        res = 0
        sum_till_now = 0

        for i in range(len(nums)):
            sum_till_now += nums[i]
            
            if(sum_till_now - k in prefix_sum):
                res += prefix_sum[sum_till_now - k]

            if(sum_till_now in prefix_sum):
                prefix_sum[sum_till_now] += 1
            else:
                prefix_sum[sum_till_now] = 1

        return res