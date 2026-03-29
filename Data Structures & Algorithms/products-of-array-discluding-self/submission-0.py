class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        num_zeros = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                p *= nums[i]
            else:
                num_zeros += 1
                if(num_zeros == 2):
                    return [0 for _ in range(len(nums))]
        
        res = []
        if(num_zeros == 0):
            for i in range(len(nums)):
                res.append(p // nums[i])
        else:
            for i in range(len(nums)):
                if(nums[i] == 0):
                    res.append(p)
                else:
                    res.append(0)
        
        return res
