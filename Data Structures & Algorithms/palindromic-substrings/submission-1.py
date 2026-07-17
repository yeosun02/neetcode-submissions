class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [1] * n
        l = r = 0
        for i in range(n):
            if r > i:
                p[i] = min(p[l + r - i], r - i)

            while (i - p[i] >= 0 and i + p[i] < n and t[i + p[i]] == t[i - p[i]]):
                p[i] += 1
            
        return sum([i // 2 for i in p])