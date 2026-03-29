class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda l:l[0])
        res = 0

        cur_interval = intervals[0]
        for i in range(1, len(intervals)):
            next_interval = intervals[i]

            if(cur_interval[1] <= next_interval[0]):
                #Non-overlapping
                cur_interval = next_interval
            else:
                if(cur_interval[1] > next_interval[1]):
                    #Remove the current
                    cur_interval = next_interval
                    
                res += 1

        return res