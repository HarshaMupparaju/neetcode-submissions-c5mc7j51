class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res_s = set()

        def dfs(arr: List[int], cur: List[int]) -> None:
            if(len(cur) == len(nums)):
                res_s.add(tuple(cur.copy()))

            arr_copy = arr.copy()

            for i in range(len(arr_copy)):
                cur.append(arr[i])
                temp = arr.pop(i)
                dfs(arr, cur)
                arr.insert(i, temp)
                cur.pop()


        dfs(nums.copy(), [])

        res = []

        for key in res_s:
            res.append(list(key))

        return res