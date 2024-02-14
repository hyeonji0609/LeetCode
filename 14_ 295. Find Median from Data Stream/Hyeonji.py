class MedianFinder:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, (num, num))
    
    def findMedian(self) -> float:
        temp_heap = self.heap[:]
        
        quotient, remainder = divmod(len(temp_heap), 2)
        
        if remainder == 0:
            if quotient == 1:
                self.median = (temp_heap[0][0] + temp_heap[1][0]) / 2
            else:
                self.median = (temp_heap[quotient-1][0] + temp_heap[quotient][0]) / 2
        else:
            self.median = temp_heap[quotient][0]
        
        return self.median
                
        
#         heapq.heapify(temp_heap)
        
#         quotient, remainder = divmod(len(temp_heap), 2)
        
#         first = 0
#         second = 0
#         median = 0

#         if remainder == 0:
#             if quotient == 1:
#                 first = heapq.heappop(temp_heap)
#                 second = heapq.heappop(temp_heap)
#                 median = (first + second) / 2
#             else:
#                 for _ in range(quotient):
#                     first = heapq.heappop(temp_heap)
#                 second = heapq.heappop(temp_heap)
#                 median = (first + second) / 2
#         else:
#             if quotient == 1 or quotient == 0:
#                 for _ in range(quotient+1):
#                     median = heapq.heappop(temp_heap)
#             else:
#                 for _ in range(quotient+1):
#                     median = heapq.heappop(temp_heap)
        
#         return median

"""
Time Limit Exceed
"""