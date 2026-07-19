class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        l, r = 0, n
        while l < r:
            m = (l + r) >> 1
            if intervals[m][1] < newInterval[0]:
                l = m + 1
            else:
                r = m
        
        if l == n:
            intervals.append(newInterval)
            return intervals

        st = min(intervals[l][0], newInterval[0])
        cur_end = newInterval[1]
        idx = l
        while idx < n and intervals[idx][0] <= cur_end:
            cur_end = max(intervals[idx][1], cur_end)
            idx += 1
        
        intervals = intervals[:l] + [[st, cur_end]] + intervals[idx:]
        return intervals
