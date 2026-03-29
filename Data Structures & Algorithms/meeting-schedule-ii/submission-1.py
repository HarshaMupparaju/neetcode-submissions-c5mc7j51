"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        count = 0
        n = len(intervals)

        # intervals.sort(key = lambda l: l.start)

        start = []
        end = []

        for i in range(len(intervals)):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort()
        end.sort()
        
        start_pointer = 0
        end_pointer = 0

        while(start_pointer < n and end_pointer < n):
            if(start[start_pointer] < end[end_pointer]):
                #A meeting has started
                count += 1
                res = max(res, count)
                start_pointer += 1
            else:
                #A meeting has ended
                count -= 1
                end_pointer += 1
        
        return res