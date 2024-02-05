import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1, 1001))

    def popSmallest(self) -> int:
        min_num = heapq.heappop(self.heap)
        return min_num

    def addBack(self, num: int) -> None:
        if not num in self.heap:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)

"""
Runtime 156 ms
Memory 17.54 MB
"""