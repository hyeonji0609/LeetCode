import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 최대힙을 담을 리스트 초기화
        heap = []
        # 힙 구성(-item으로 최대힙 구현)
        for item in nums:
            heapq.heappush(heap, (-item, item))
        
        # k번째 큰 값을 저장할 변수 초기화
        kth_max = None
        # 루프를 돌면서 k번째로 큰 값 저장
        for _ in range(k):
            kth_max = heapq.heappop(heap)
        
        # k번째로 큰 값은 튜플이므로 key가 아닌 value를 리턴
        return kth_max[1]
    
    '''
    Runtime 620 ms - Beats 17.42%
    Memory 36.20 MB - Beats 5.22%
    '''