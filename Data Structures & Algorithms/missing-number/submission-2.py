class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if(i ^ nums[i] != 0):
                return i
        
        if(len(nums) ^ nums[-1] != 0):
            return len(nums)