class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #TC: O(2n), SC: O(2n)
        ans = [0] * (2 * len(nums)) 
        # for i in range(2):
        for j in range(len(nums)):
            ans[j] = nums[j]
            ans[j + len(nums)] = nums[j]
        
        return ans