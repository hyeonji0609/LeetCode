class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.items = []
        
    def insertFront(self, value: int) -> bool:
        if len(self.items) == self.k :
            return False
        else :
            self.items.insert(0, value)
            return True

    def insertLast(self, value: int) -> bool:
        if len(self.items) == self.k :
            return False
        else :
            self.items.append(value)
            return True
        
    def deleteFront(self) -> bool:
        if len(self.items) == 0 :
            return False
        else :
            self.items.pop(0)
            return True
        
    def deleteLast(self) -> bool:
        if len(self.items) == 0 :
            return False
        else :
            self.items.pop(-1)
            return True

    def getFront(self) -> int:
        if len(self.items) == 0:
            return -1
        else :
            return self.items[0]

    def getRear(self) -> int:
        if len(self.items) == 0:
            return -1
        else :
            return self.items[-1]
        
    def isEmpty(self) -> bool:
        if len(self.items) == 0:
            return True
        else :
            return False

    def isFull(self) -> bool:
        if len(self.items) == self.k:
            return True
        else :
            return False

"""
Runtime: 49 ms
Memory Usage: 17.2 MB
"""