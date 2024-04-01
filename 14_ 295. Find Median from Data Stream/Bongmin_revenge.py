import heapq
## 진짜 어떻게 풀 지 몰라서 주석으로만 달아놓습니다 .. 
class MedianFinder:
    def __init__(self):
        self.low = []  # 최대 힙 # 작은 것들에서는 값이 높은 애들
        self.high = []  # 최소 힙 # 큰 것들에서는 값이 작은 애들

    def addNum(self, num):
        heapq.heappush(self.low, -num) # 먼저 최대 힙에 -를 붙여서 저장
        heapq.heappush(self.high, -self.low[0]) # 최대 힙에 있는 처음 것을 최소 힙에 저장
        heapq.heappop(self.low) # 최대 힙에서 최대 값을 꺼내고
        
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -self.high[0])
            heapq.heappop(self.high)
            
    def findMedian(self):
        if len(self.low) > len(self.high):
            return -self.low[0]                  
        else:
            return (self.high[0] - self.low[0]) / 2 
