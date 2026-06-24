class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # max_s = max(intervals)[0]
        # max_e = max(intervals, key=lambda i:i[1])[1] + 1
        # ends = [max_e] * (max_s + 1)
        ends = {}
        res = 0
        for s, e in intervals:
            if s in ends:
                res += 1
                ends[s] = min(ends[s], e)
            else:
                ends[s] = e
        
        ends = dict(sorted(ends.items()))
        last_e = -float('inf')
        for s, e in ends.items():
            if s < last_e:
                res += 1
                last_e = min(last_e, e)
            else:
                last_e = e
        
        return res
        # for s, e in intervals:
        #     s += NO_NEGATIVE
        #     if ends[s] != max_e:
        #         res += 1
        #         ends[s] = min(ends[s], e)
        #     else:
        #         ends[s] = e
        
        # last_e = -1
        # for i in range(max_s):
        #     if ends[i] == max_e:
        #         continue
            
        #     if i - NO_NEGATIVE < last_e:
        #         res += 1
        #         last_e = min(last_e, ends[i])
        #     else:
        #         last_e = ends[i]
        
        # return res