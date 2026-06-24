class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        inserted = False
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            idx += 1
        
        if idx < len(intervals):
            newInterval[0] = min(intervals[idx][0], newInterval[0])
        
        next_i = idx
        while next_i < len(intervals) and intervals[next_i][0] <= newInterval[1]:
            newInterval[1] = max(intervals[next_i][1], newInterval[1])
            next_i += 1
        
        return intervals[:idx] + [newInterval] + intervals[next_i:]