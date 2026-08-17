class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        d = {}
        res = []
        perm = []

        for num in nums:
            if(num in d):
                d[num] += 1
            else:
                d[num] = 1
            
        def dfs() -> None:
            if(len(perm) == len(nums)):
                res.append(perm.copy())
                return
            
            for n in d:
                if(d[n] > 0):
                    perm.append(n)
                    d[n] -= 1
                
                    dfs()

                    d[n] += 1
                    perm.pop()
            
            return

        dfs()
        return res


        # #TC: O(n x n!), SC: O(n!/sum_i(i!) n)
        # res_s = set()

        # def dfs(arr: List[int], cur: List[int]) -> None:
        #     if(len(cur) == len(nums)):
        #         res_s.add(tuple(cur.copy()))

        #     arr_copy = arr.copy()

        #     for i in range(len(arr_copy)):
        #         cur.append(arr[i])
        #         temp = arr.pop(i)
        #         dfs(arr, cur)
        #         arr.insert(i, temp)
        #         cur.pop()

        # dfs(nums.copy(), [])

        # res = []

        # for key in res_s:
        #     res.append(list(key))

        # return res