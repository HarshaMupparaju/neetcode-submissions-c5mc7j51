import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        triplets = sorted(zip(startTime, endTime, profit))

        startTime = []
        endTime = []
        profits = []

        dp = [-1] * (n+1) 

        for s, e, p in triplets:
            startTime.append(s)
            endTime.append(e)
            profits.append(p)

        def dfs(index: int):
            if(index >= n):
                dp[index] = 0
                return dp[index]

            if(dp[index] != -1):
                return dp[index]

            #We take this
            # next_viable_index = n
            
            # #Binary Search
            # val = endTime[index]
            # left = index + 1
            # right = n - 1
            # while(left <= right):
            #     mid = (left + right) // 2

            #     if(startTime[mid] >= val):
            #         right = mid - 1
            #         next_viable_index = mid
            #     else:
            #         left = mid + 1

            # Binary Search library
            next_viable_index = bisect.bisect_left(startTime, endTime[index]) #The first index where startTime >= endTime

            res1 = profits[index] + dfs(next_viable_index)

            #We don't take this
            res2 = dfs(index + 1)
            dp[index] = max(res1, res2)

            return dp[index]

        _ = dfs(0)

        return dp[0]