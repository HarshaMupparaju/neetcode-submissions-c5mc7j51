class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = 0
        whites = 0
        blues = 0

        for i in range(len(nums)):
            if(nums[i] == 0):
                reds += 1
            elif(nums[i] == 1):
                whites += 1
            else:
                blues += 1
        
        cur = 0

        while(reds > 0):
            nums[cur] = 0
            reds -= 1
            cur += 1
        
        while(whites > 0):
            nums[cur] = 1
            whites -= 1
            cur += 1
        
        while(blues > 0):
            nums[cur] = 2
            blues -= 1
            cur += 1
        
        return 
