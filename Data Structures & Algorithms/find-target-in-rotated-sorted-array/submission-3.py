class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while(l <= r):
            mid = (l + r) // 2

            if(nums[mid] == target):
                return mid

            if(nums[l] <= nums[mid]): #Left half is sorted
                if(nums[l] <= target < nums[mid]):
                    #Move left
                    r = mid
                else:
                    l = mid + 1

            else: #Right half is sorted
                if(nums[mid] < target <= nums[r]):
                    #Move Right
                    l = mid + 1
                else:
                    r = mid

        return -1