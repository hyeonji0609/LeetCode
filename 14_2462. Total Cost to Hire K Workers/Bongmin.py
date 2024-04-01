import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i = 0 # i는 0부터 시작하는 인덱스 tracking
        j = len(costs) - 1 # j는 맨 끝부터 시작하는 인덱스 tracking
        
        # 힙 pq1과 pq2 초기화
        pq1 = [] # 처음부터 시작하는
        pq2 = [] # 맨 뒤부터 시작하는 
        
        # 총 비용 변수 초기화
        ans = 0
        
        # K가 0이 아닐 때 까지
        while k > 0:
            # pq1에 candidates만큼 추가
            while len(pq1) < candidates and i <= j:
                heapq.heappush(pq1, costs[i])
                i += 1
            
            # pq2에 candidates만큼 추가
            while len(pq2) < candidates and i <= j:
                heapq.heappush(pq2, costs[j])
                j -= 1
            
            # pq1과 pq2의 최솟값 중 작은 값을 t1과 t2에 저장
            t1 = pq1[0] if pq1 else float('inf')
            t2 = pq2[0] if pq2 else float('inf')
            
            # t1이 작다면
            if t1 <= t2:
                ans += t1 # t1만큼 더하고
                heapq.heappop(pq1) # t1을 제거
            # 반대
            else: 
                ans += t2
                heapq.heappop(pq2)
            
            # 라운드 하나 -1
            k -= 1
        
        # 총 비용 반환
        return ans