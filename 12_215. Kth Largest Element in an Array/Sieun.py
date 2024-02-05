from heapq import nlargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]

"""
Runtime 560 ms
Memory 34.02 MB
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        len_nums = len(nums)
        heapq.heapify(nums)
        nth_max = None

        for _ in range(len_nums-k+1):
            nth_max = heapq.heappop(nums)
        
        return nth_max

"""
Runtime 500 ms
Memory 28.80 MB
"""