class Solution:
    def check_distinct(self, i: int, j: int, nums: List[int], d: Dict):

        if(-nums[i]-nums[j] in d):
            for k in range(len(d[-nums[i] - nums[j]])):
                if(d[-nums[i] - nums[j]][k] != i and d[-nums[i] - nums[j]][k] != j):
                    return (tuple(sorted([nums[i], nums[j], nums[d[-nums[i] - nums[j]][k]]])))

        return None


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}

        res = set()

        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]].append(i)
            else:
                d[nums[i]] = [i]
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = self.check_distinct(i, j, nums, d)
                if(temp is not None):
                    res.add(temp)

        final_res = [[ai,aj,ak] for ai,aj,ak in res]
        print(final_res)
        return final_res