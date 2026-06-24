import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res
        # hp = []
        # res = []

        # for i in range(k - 1):
        #     heapq.heappush(hp, (-nums[i], i))

        # for i in range(k - 1, len(nums)):
        #     heapq.heappush(hp, (-nums[i], i))
        #     while hp[0][1] <= i - k:
        #         heapq.heappop(hp)
            
        #     res.append(-hp[0][0])

        # return res