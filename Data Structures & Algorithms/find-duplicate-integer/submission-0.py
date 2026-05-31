class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(fast == slow):
                break
        

        # print(nums[slow])
        # print(1/0)
        slow2 = 0

        while(slow != slow2):
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow