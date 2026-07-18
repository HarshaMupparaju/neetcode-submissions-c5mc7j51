class Solution:
    def findMin(self, nums: List[int]) -> int:
        #TC: O(log n); SC: O(1)
        l = 0
        r = len(nums) - 1

        while(l < r):
            mid = (l + r) // 2

            if(nums[mid] < nums[r]):
                r = mid
            else:
                l = mid + 1

        return nums[l]