class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal_post = n - 1
        res = False

        for i in range(n - 1, -1, -1):
            if(i + nums[i] >= goal_post):
                goal_post = i
        
        if(goal_post == 0):
            res = True
        
        return res
        