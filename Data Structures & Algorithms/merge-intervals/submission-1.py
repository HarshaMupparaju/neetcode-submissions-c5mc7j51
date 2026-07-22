class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        
        intervals.sort()
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            if(intervals[i][0] <= res[-1][1]):
                #overlap
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                #no overlap
                res.append(intervals[i])

        return res