"""
https://leetcode.com/problems/find-median-from-data-stream/
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.size = 0
        self.median = 0.0

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.size += 1
        self.nums.sort()
        if self.size % 2 != 0:
            self.median = self.nums[self.size // 2]
            # print(self.nums)
        else:
            # print(self.size, self.size//2)
            # print(self.nums)
            self.median = (self.nums[self.size // 2 - 1] + self.nums[self.size // 2]) / 2
            # print(self.median)

    def findMedian(self) -> float:
        return self.median


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

m = MedianFinder()
m.addNum(6)
print(m.findMedian())  # 6
m.addNum(10)
print(m.findMedian())  # 8
m.addNum(2)
print(m.findMedian())  # 6
m.addNum(6)
print(m.findMedian())  # 6
m.addNum(5)
print(m.findMedian())
m.addNum(0)
print(m.findMedian())
m.addNum(6)
print(m.findMedian())
m.addNum(3)
print(m.findMedian())
m.addNum(1)
print(m.findMedian())
m.addNum(0)
print(m.findMedian())
m.addNum(0)
"""
["MedianFinder","addNum","findMedian","addNum","findMedian","addNum",
"findMedian","addNum","findMedian","addNum","findMedian","addNum",
"findMedian","addNum","findMedian","addNum","findMedian","addNum",
"findMedian","addNum","findMedian","addNum","findMedian"]
[[],[6],[],[10],[],[2],[],[6],[],[5],[],[0],[],[6],[],[3],[],[1],[],[0],[],[0],[]]
"""
