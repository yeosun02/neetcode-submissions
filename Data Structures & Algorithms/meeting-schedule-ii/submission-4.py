from bisect import insort
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        st, et = [], []
        for i in intervals:
            insort(st, i.start)
            insort(et, i.end)

        s, e = 0, 0
        days = c = 0
        while s < n:
            if st[s] < et[e]:
                c += 1
                s += 1
            else:
                e += 1
                c -= 1
            days = max(days, c)
        
        return days