class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        overlaps = [0] * len(intervals)

        for i, interval in enumerate(intervals):
            if( (interval[0] <= newInterval[0] <= interval[1]) or \
                (interval[0] <= newInterval[1] <= interval[1]) or \
                (interval[0] >= newInterval[0] and interval[1] <= newInterval[1])):
                overlaps[i] = 1
            
        res = []


        min_int = newInterval[0]
        max_int = newInterval[1]

        flag = 0

        for i in range(len(intervals)):
            if(flag == 0 and intervals[i][0] > max_int):
                res.append([min_int, max_int])
                flag = 1
                
            if(overlaps[i] == 0):
                res.append(intervals[i])
            else:
                min_int = min(min_int, intervals[i][0])
                max_int = max(max_int, intervals[i][1])
        
        if(flag == 0):
            #Only 1 fully overlapping interval
            res.append([min_int, max_int])

        return res
            
