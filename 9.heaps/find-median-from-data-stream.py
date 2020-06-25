class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            if num > self.findMedian():
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -1 * num)
        elif len(self.min_heap) > len(self.max_heap):
            if num > self.min_heap[0]:
                switch_num = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -1 * switch_num)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -1 * num)
        else:
            if num < self.max_heap[0] * -1:
                switch_num = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, switch_num * -1)
                heapq.heappush(self.max_heap, num * -1)
            else:
                heapq.heappush(self.min_heap, num)

    def findMedian(self) -> float:
        if len(self.min_heap) == 0 and len(self.max_heap) == 0:
            return float("inf")
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0] * -1
        else:  # len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -1 * self.max_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()