# https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq

class MedianFinder:

    def __init__(self):

        self.small = []
        self.large = []

        self.count_small = 0
        self.count_large = 0

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.small, -num)
        self.count_small += 1

        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            self.count_small -= 1
            heapq.heappush(self.large, val)
            self.count_large += 1

        if self.count_small > self.count_large + 1:
            val = -heapq.heappop(self.small)
            self.count_small -= 1
            heapq.heappush(self.large, val)
            self.count_large += 1

        if self.count_large > self.count_small + 1:
            val = heapq.heappop(self.large)
            self.count_large -= 1
            heapq.heappush(self.small, -val)
            self.count_small += 1
        

    def findMedian(self) -> float:

        if self.count_small == self.count_large + 1:
            return -self.small[0]
        elif self.count_small + 1 == self.count_large:
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
