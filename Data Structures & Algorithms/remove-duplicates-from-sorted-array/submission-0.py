class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        ptr = 0
        #[2, 10, 10, 30, 30, 30]
        cur = float('-inf')
        for i in range(len(nums)):
            if(nums[i] != cur):
                #New unique element
                cur = nums[i]
                nums[ptr] = nums[i]
                ptr += 1
                k += 1

        return k