class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_s = max(intervals, key=lambda item: item[0])[0]
        ends = [0] * (max_s + 1)
        for s, e in intervals:
            ends[s] = max(e + 1, ends[s])
        
        res = []
        cur_e = -1
        cur_s = max_s + 1
        for i in range(max_s + 1):
            if ends[i] != 0:
                cur_s = min(cur_s, i)
                cur_e = max(cur_e, ends[i] - 1)
            
            if i == cur_e:
                res.append([cur_s, cur_e])
                cur_s = max_s + 1
                cur_e = 0

        if cur_s != max_s + 1:
            res.append([cur_s, cur_e])
        
        return res

        # intervals.sort(key=lambda item: item[0])
        # res = []
        # last_s = last_e = intervals[0][0]
        # for s, e in intervals:
        #     if s > last_e:
        #         res.append([last_s, last_e])
        #         last_s = s
        #     last_e = max(last_e, e)
        
        # res.append([last_s, last_e])
        # return res