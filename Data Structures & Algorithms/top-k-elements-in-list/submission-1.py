class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for num, cnt in freq.items():
            buckets[cnt].append(num)
        
        res = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res