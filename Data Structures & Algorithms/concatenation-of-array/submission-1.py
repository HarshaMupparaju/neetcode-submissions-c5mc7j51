class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #TC: O(2n), SC: O(2n)
        ans = []
        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])
        
        return ans