class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # since we know |stone| <= 100
        freq = [0] * 101
        for stone in stones:
            freq[stone] += 1
        
        weight = 100
        max1 = max2 = 0
        while weight > 0:
            if freq[weight]:
                max1, max2 = max2, weight
                freq[weight] -= 1
            
                if max1:
                    freq[max1 - max2] += 1
                    weight = max(weight, max1 - max2)
                    max2 = 0
            else:
                weight -= 1
        
        return max2

        #
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            diff = stone1 - stone2
            if diff:
                heapq.heappush(max_heap, -diff)
        
        return -max_heap[0] if max_heap else 0