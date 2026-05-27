class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}

        for i in range(len(s)):
            if(s[i] in d):
                d[s[i]][1] = i
            else:
                d[s[i]] = [i, i]
        
        # print(d)


        #Merge Overlapping Intervals
        intervals = []

        for k in d:
            intervals.append(d[k])
        
        intervals.sort()

        # print(intervals)

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            if(merged_intervals[-1][1] >= intervals[i][0]):
                merged_intervals[-1][0] = min(merged_intervals[-1][0], intervals[i][0])
                merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])
            else:
                merged_intervals.append(intervals[i])

        #Get outoput

        print(merged_intervals)

        res = []

        for m in merged_intervals:
            res.append(m[1] - m[0] + 1)


        return res