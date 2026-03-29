class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while(l <= r):
            mid = (l + r) // 2
            print(mid)
            if(nums[mid] == target):
                return mid
            elif(nums[l] == target):
                return l
            elif(nums[r] == target):
                return r

            if(nums[mid] > nums[l] and target > nums[l] and target < nums[mid]):
                #Left side is sorted
                #Target is in the sorted half
                r = mid - 1
            elif(nums[mid] > nums[l] and (target < nums[l] or target > nums[mid])):
                #Left side is sorted
                #Target is in the unsorted half
                l = mid + 1
            elif(nums[mid] < nums[l] and target > nums[mid] and target < nums[r]):
                #Right side is sorted
                #Target is in the sorted half
                l = mid + 1
            else:
                r = mid - 1
        
        return -1