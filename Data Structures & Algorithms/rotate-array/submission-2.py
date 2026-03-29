class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            end = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            
            nums[0] = end

        # temp = []
        
        # for i in range(-k,0, 1):
        #     temp.append(nums[i])
        
        # for i in range(len(nums) - k - 1, -1, -1):
        #     nums[i + k] = nums[i]
        
        # for i in range(len(temp)):
        #     nums[i] = temp[i]
        
        return 
        