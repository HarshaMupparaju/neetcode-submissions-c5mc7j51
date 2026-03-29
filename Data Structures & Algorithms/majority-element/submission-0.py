class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}

        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        for k in d:
            if(d[k] >= (n // 2)):
                return k
        
        return 0