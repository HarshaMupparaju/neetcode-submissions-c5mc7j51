class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #TC: O(2n + m), SC: O(n * m)
        #Add all elements to a dict, with indices
        res = []
        d = {}

        for i, num in enumerate(nums):
            if(num in d):
                d[num].append(i)
            else:
                d[num] = [i]
        
        #Iterate through the array and check for target - nums[i] in the dict

        for i, num in enumerate(nums):
            if((target - num) in d):
                for j in d[target - num]:
                    if(j != i):
                        res.append(i)
                        res.append(j)
                        return res

        # #Return the result array
        # return res