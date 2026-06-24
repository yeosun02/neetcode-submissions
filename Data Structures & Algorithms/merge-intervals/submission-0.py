class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: (item[0], item[1]))
        res = []
        last_s = last_e = intervals[0][0]
        for s, e in intervals:
            if s > last_e:
                res.append([last_s, last_e])
                last_s = s
            last_e = max(last_e, e)
        
        res.append([last_s, last_e])
        return res