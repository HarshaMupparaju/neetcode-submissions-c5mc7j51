class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        if(len(nums) == 0):
            return res
        else:
            res.append([])
            res.append([nums[0]])

        def make_subsets(i: int) -> None:
            nonlocal res
            if(i == len(nums)):
                return

            temp = []

            for j in range(len(res)):
                temp.append(res[j])
                temp.append(res[j] + [nums[i]])
            
            print(temp)
            res = temp
            make_subsets(i + 1)
            return



        make_subsets(1)

        return res