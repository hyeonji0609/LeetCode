class RecentCounter:

    def __init__(self):
        self.queue = []
        self.number = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        
        range_min = t-3000
        range_max = t
        self.number = 0
        
        for i in self.queue:
            if range_min <= i <= range_max:
                self.number += 1
        
        return self.number
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
Runtime: 7618 ms
Memory Usage: 23.2 MB
"""