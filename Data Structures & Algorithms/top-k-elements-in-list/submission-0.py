class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
            
            buckets[freq[num]].append(num)
        
        res = []
        count = 0
        for i in range(n, -1, -1):
            for num in buckets[i]:
                if i == freq[num]:
                    res.append(num)
                    count += 1
                if count == k:
                    break
            if count == k:
                break
        
        return res