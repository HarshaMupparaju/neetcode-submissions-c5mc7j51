"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)

        start.sort()
        end.sort()
        
        start_ptr = 0
        end_ptr = 0
        count = 0
        res = 0

        while(start_ptr < len(intervals)):
            print(start_ptr)
            print(end_ptr)

            if(start[start_ptr] < end[end_ptr]):
                count += 1
                start_ptr += 1
            elif(end[end_ptr] < start[start_ptr]):
                count -= 1
                end_ptr += 1
            else:
                start_ptr += 1
                end_ptr += 1
            
            res = max(res, count)



        return res