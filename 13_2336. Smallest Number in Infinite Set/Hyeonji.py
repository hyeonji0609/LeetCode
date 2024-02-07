class SmallestInfiniteSet:

    def __init__(self):
        self.infSet = list(range(1, 1001))

    def popSmallest(self) -> int:
        minValue = min(self.infSet)
        self.infSet.remove(minValue)
        return minValue

    def addBack(self, num: int) -> None:
        if num in self.infSet:
            return None
        else :
            self.infSet.append(num)
            return None

"""
Runtime: 376 ms
Memory Usage: 17.2 MB
"""
        
