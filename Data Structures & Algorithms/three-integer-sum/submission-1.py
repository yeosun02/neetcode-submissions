class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        res = []
        avail = list(sorted(set(freq.keys())))
        for l, num in enumerate(avail):
            target = -num
            freq[num] -= 1
            r = len(avail) - 1
            while l <= r:
                l_val, r_val = avail[l], avail[r]
                if l_val + r_val == target:
                    if ((l != r and freq[l_val] > 0 and freq[r_val] > 0)
                        or (l == r and freq[l_val] > 1)):
                        res.append([num, l_val, r_val])
                    l += 1
                    r -= 1
                elif l_val + r_val < target:
                    l += 1
                else:
                    r -= 1
            
            freq[num] += 1
        
        return res