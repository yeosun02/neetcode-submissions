class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def found_all(freq: dict[int]) -> bool:
            for v in freq.values():
                if v > 0:
                    return False
            
            return True

        freq = {}
        for char in t:
            freq[char] = 1 + freq.get(char, 0)
        
        l = 0
        max_l = 0
        min_r = len(s) - 1
        all_found = False
        for r, char in enumerate(s):
            if char in freq:
                freq[char] -= 1
                if not all_found:
                    all_found = found_all(freq)
            
            while l < len(s) and (s[l] not in freq or freq[s[l]] < 0):
                if s[l] in freq:
                    freq[s[l]] += 1
                l += 1
            
            if all_found and r - l < min_r - max_l:
                max_l, min_r = l, r
        
        if not all_found:
            return ""

        return s[max_l:min_r + 1]

        # def diff_freq(freq: List[int], encode: str) -> str:
        #     ls = encode.split("#")
        #     for i in range(len(ls)):
        #         ls[i] = int(ls[i]) - freq[i]
        #         if ls[i] < 0:
        #             return ""
            
        #     return "#".join(map(str, ls))

        # indices = {char: i for i, char in enumerate(set(t))}
        # freq = ["0"] * len(set(t))
        # pref = {"#".join(freq): [0, 0]}
        # for i in range(len(s)):
        #     if s[i] in t:
        #         pref["#".join(freq)][1] = i

        #         idx = indices[s[i]]
        #         freq[idx] = str(int(freq[idx]) + 1)
        #         pref["#".join(freq)] = [i, i]

        #     pref["#".join(freq)][1] = i
        
        # freq = [0] * len(set(t))
        # for char in t:
        #     freq[indices[char]] += 1
            
        # target = "#".join(map(str, freq))
        # if target not in pref:
        #     return ""

        # res = [0, len(s) - 1]
        # for k, [i_s, i_e] in pref.items():
        #     target = diff_freq(freq, k)
        #     if target == "" or target not in pref:
        #         continue

        #     _, i_e2 = pref[target]
        #     if i_s - i_e2 < res[1] - res[0]:
        #         res = [i_e2, i_s]

        # return s[res[0]:res[1] + 1]

