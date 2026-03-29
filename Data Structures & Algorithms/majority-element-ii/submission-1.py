class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        res = []

        for i in range(n):
            if(nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
            
            if(d[nums[i]] > n // 3):
                res.append(nums[i])
                d[nums[i]] = - 10 ** 6
        
        return res
    