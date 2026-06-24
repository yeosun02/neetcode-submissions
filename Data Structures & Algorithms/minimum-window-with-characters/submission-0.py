class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def minDiff(l, r):
            if r == 0:
                return l
            return min((l, r), key=lambda item: item[1] - item[0])

        n = len(s)
        m = len(t)

        counter = Counter(t)
        tot_cnt = 0
        idx_list = []
        length = 0
        f_loc = 0
        
        for i, char in enumerate(s):
            if char in counter:
                counter[char] -= 1
                idx_list.append(i)
                if counter[char] >= 0:
                    tot_cnt += 1
            
                if tot_cnt < m:
                    continue
                
                length = minDiff((idx_list[f_loc], idx_list[-1]), length)
                tot_cnt -= 1

                while counter[s[idx_list[f_loc]]] < 0:
                    new_l = (idx_list[f_loc + 1], idx_list[-1])
                    length = minDiff(new_l, length)
                    counter[s[idx_list[f_loc]]] += 1
                    f_loc += 1
                else:
                    counter[s[idx_list[f_loc]]] += 1
                    f_loc += 1

        if length == 0:
            return ""
        return s[length[0]: length[1] + 1]