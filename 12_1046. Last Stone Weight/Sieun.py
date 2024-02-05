class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            A = stones.pop()
            B = stones.pop()

            if A > B:
                stones.append(A-B)
        
        if stones:
            return stones[0]
        else:
            return 0

"""
Runtime 46 ms
Memory 16.56 MB
"""

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            A = heapq.heappop(max_heap)
            B = heapq.heappop(max_heap)

            if A < B:
                heapq.heappush(max_heap, A-B)
        
        if max_heap:
            return -heapq.heappop(max_heap)
        else:
            return 0

"""
Runtime 43 ms
Memory 16.52 MB
"""