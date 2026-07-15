"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # simple sorting
        if not intervals:
            return True
            
        intervals = sorted(intervals, key=lambda item: item.start)
        prev = intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start < prev:
                return False
            prev = intervals[i].end
        
        return True
        # 
        end_time = {}
        s_time = []

        def get_r_index(target, items):
            l, r = 0, len(items)
            while l < r:
                m = (l + r) >> 1
                if target < items[m]:
                    r = m
                else:
                    l = m + 1
            return l

        for interval in intervals:
            s, e = interval.start, interval.end
            if not s_time:
                s_time.append(s)
                end_time[s] = e
                continue
            
            idx = get_r_index(s, s_time)
            print(idx, s_time, end_time)
            if idx > 0 and end_time[s_time[idx - 1]] > s:
                return False
            
            if idx < len(s_time) and s_time[idx] < e:
                return False

            if idx == len(s_time):
                s_time.append(s)
            else:
                s_time.insert(idx, s)
            
            end_time[s] = e
        
        return True
            

            