class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates = sorted(candidates)

        subset = []
        subset_sum = [0]
        def dfs(i: int):


            if(i == len(candidates)):
                if(subset_sum[0] == target):
                    res.append(subset.copy())
                return

            if(subset_sum[0] > target):
                return
            
            #We choose candidate i
            subset.append(candidates[i])
            subset_sum[0] += candidates[i]
            dfs(i + 1)

            #We don't choose candidate i
            subset.pop()
            subset_sum[0] -= candidates[i]
            while(i + 1 < len(candidates) and candidates[i + 1] == candidates[i]):
                i += 1
            
            dfs(i + 1)

        dfs(0)

        return res