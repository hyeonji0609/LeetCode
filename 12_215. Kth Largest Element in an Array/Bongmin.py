'''nlargest는 큰 순서대로 n개의 리스트를 반환한다, nsmallest도 있다!'''

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = heapq.nlargest(k, nums) # 큰 순서대로 k개를 찾겠다.
        return largest[-1] # 큰 순서대로 찾으므로 마지막을 반환한다
    

