import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)

        top_elems = []

        for key, val in frequency.items():
            heapq.heappush(top_elems, (val, key))

            if len(top_elems) > k:
                heapq.heappop(top_elems)
        
        return [elem[1] for elem in top_elems]