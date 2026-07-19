class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i: int, cur_sum: int, arr: List[int]) -> None:
            if(cur_sum == target):
                res.append(arr.copy())
                # res.add(tuple(arr.copy()))
                return
            
            if(cur_sum > target):
                return
            
            if(i >= len(nums)):
                return
            
            #Dont pick, go next
            dfs(i + 1, cur_sum, arr)

            arr.append(nums[i])

            #Pick, stay
            dfs(i, cur_sum + nums[i], arr)

            arr.pop()

            return

        dfs(0, 0, [])

        # final = []

        # for key in res:
        #     final.append(list(key))

        return res

