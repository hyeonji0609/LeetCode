class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = []
        self.k = k

    def insertFront(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if not self.deque:
            return False
        else:
            del self.deque[0]
            return True

    def deleteLast(self) -> bool:
        if not self.deque:
            return False
        else:
            self.deque.pop()
            return True

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if not self.deque:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.deque) == self.k:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

"""
Runtime 57 ms
Memory 17.18 MB
"""