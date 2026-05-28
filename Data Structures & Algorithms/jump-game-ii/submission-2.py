class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i = 0
        res = 0

        while(i < len(nums) - 1):
            max_jump = nums[i]
            print(i)
            best_jump = float('-inf')
            temp = 0
            for j in range(1, max_jump + 1):
                if(i + j >= len(nums) - 1):
                    temp = len(nums) - 1
                    break
                # print(nums[i + j])

                if(j + nums[i + j] >= best_jump):
                    best_jump = j + nums[i + j]
                    temp = i + j

            i = temp
            res += 1
            
        return res
            