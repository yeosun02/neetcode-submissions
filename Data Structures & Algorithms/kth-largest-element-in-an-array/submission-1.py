class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in range(k):
            q.append(nums[i])
        heapq.heapify(q)
        for i in range(k, len(nums)):
            if q[0] < nums[i]:
                heapq.heappop(q)
                heapq.heappush(q, nums[i])
        return q[0]
        # return sorted(nums, reverse=True)[k - 1]