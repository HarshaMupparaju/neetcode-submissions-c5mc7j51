class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #TC: O(n), SC: O(n)
        d = {} #num, index

        for i, num in enumerate(nums):
            if(target - num in d):
                return [d[target - num] , i]
            d[num] = i
        
        return

