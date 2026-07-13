class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = {}

        for num in nums:
            if(num in d):
                d[num] += 1
            else:
                d[num] = 1
        
        count = [[] for _ in range(len(nums) + 1)]

        for key in d:
            count[d[key]].append(key)

        res = []
        for i in range(len(count) - 1, -1, -1):
            vals = count[i]

            for val in vals:
                res.append(val)
                if(len(res) == k):
                    return res


        # #TC: O(n + n log n + k log n), SC: O(n + n)
        # d = {} #count, num

        # for num in nums:
        #     if num in d:
        #         d[num] += 1
        #     else:
        #         d[num] = 1
        
        # hp = []

        # for key in d:
        #     heapq.heappush(hp, (-d[key], key))
        
        # res = []

        # for i in range(k):
        #     res.append(heapq.heappop(hp)[1])
        
        # return res

