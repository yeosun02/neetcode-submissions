"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda item: item.start)
        pq = []
        for interval in intervals:
            s, e = interval.start, interval.end
            if pq and pq[0] <= s:
                heapq.heappop(pq)

            heapq.heappush(pq, e)
        
        return len(pq)