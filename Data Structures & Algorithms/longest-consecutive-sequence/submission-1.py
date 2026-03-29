class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}

        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        max_till_now = 0

        for i in range(len(nums)):
            temp = 1
            for j in range(nums[i] + 1, 10 ** 9):
                if(j in d):
                    temp += 1
                else:
                    break
            
            max_till_now = max(temp, max_till_now)
    
        return max_till_now