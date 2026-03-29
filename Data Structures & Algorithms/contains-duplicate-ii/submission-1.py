class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        d = {}
        for i in range(len(nums)):
            if(nums[i] in d):
                for j in range(len(d[nums[i]])):
                    if(abs(i - d[nums[i]][j]) <= k):
                        return True
                
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        
        return False