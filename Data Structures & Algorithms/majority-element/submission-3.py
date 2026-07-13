class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyre-Moore Algorithm; TC: O(n) and SC: O(1)
        res = 0
        count = 0

        for num in nums:
            if(count == 0):
                res = num
            
            if(num == res):
                count += 1
            else:
                count -= 1
        
        return res

        
        # #TC: O(n) and SC: O(n)
        # d = {}

        # for num in nums:
        #     if(num in d):
        #         d[num] += 1
        #     else:
        #         d[num] = 1
            
        #     if(d[num] > len(nums) / 2):
        #         return num
        
