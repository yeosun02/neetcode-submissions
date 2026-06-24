class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        l, r = 0, self.length
        while l < r:
            m = (l + r) >> 1
            if self.arr[m] > num:
                r = m
            else:
                l = m + 1
        self.arr.insert(l, num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length & 1:
            return self.arr[self.length >> 1]
        else:
            return (self.arr[self.length >> 1] + self.arr[(self.length >> 1) - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()