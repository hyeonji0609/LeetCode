import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) # list를 heap으로 만들기
        
        for _ in range(len(nums)-k+1): 
            nth_max = heapq.heappop(nums)
        
        return nth_max
"""
Runtime: 484 ms
Memory Usage: 28.9 MB

k번째로 큰 수 == len(nums)-k+1 번째로 작은 수
ex) 총 6개의 인자를 가지고 있는 리스트에서
2번째로 가장 큰 수는 5번째로 작은 수와 같음
len(nums)-k+1 == 6-2+1
"""