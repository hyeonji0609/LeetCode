class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        len_nums = len(self.nums)

        if len_nums % 2 == 1:
            return self.nums[len_nums//2]
        else:
            return (self.nums[len_nums//2-1] + self.nums[len_nums//2])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

"""
Runtime 2413 ms
Memory 37.84 MB
"""