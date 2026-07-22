class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i, interval in enumerate(intervals):
            #newInterval, interval
            if(newInterval[1] < interval[0]):
                res.append(newInterval)
                return res + intervals[i: ]
            #interval, newInterval
            elif(newInterval[0] > interval[1]):
                res.append(interval)
            #Overlap
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        #If we never reach the return above, then we haven't added newinterval yet
        res.append(newInterval)
        return res