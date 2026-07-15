class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if len(self.large) == len(self.small):
            if self.small and num < -self.small[0]:
                heapq.heappush(self.small, -num)
                heapq.heappush(self.large, -heapq.heappop(self.small))
            else:
                heapq.heappush(self.large, num)
        else:
            if self.large and num > self.large[0]:
                heapq.heappush(self.large, num)
                heapq.heappush(self.small, -heapq.heappop(self.large))
            else:
                heapq.heappush(self.small, -num)

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] - self.small[0]) / 2
        