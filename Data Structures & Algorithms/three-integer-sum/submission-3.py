class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        s = set()

        def two_sum(target: int, index: int) -> None:
            left = 0
            right = len(nums) - 1

            while(left < right):
                if(nums[left] + nums[right] == target):
                    if(left != index and right != index):
                        s.add(tuple(sorted([nums[left], nums[right], -target])))
                    left += 1
                    right -= 1
                elif(nums[left] + nums[right] < target):
                    left += 1
                else:
                    right -= 1
            
            return 

        for i, num in enumerate(nums):
            two_sum(-num, i)
        
        res = []
        for key in s:
            res.append(list(key))
        
        return res