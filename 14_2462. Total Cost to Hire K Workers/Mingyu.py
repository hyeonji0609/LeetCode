class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        i = 0 # 앞에서부터 접근하는 index
        j = len(costs) - 1 # 뒤에서부터 접근하는 index
        pq1, pq2 = [], [] # 각각 앞과 뒤에서부터 접근하는 우선순위 큐 초기화
        
        res = 0 # result(cost)를 0으로 초기화
        while k > 0: # k번 반복
            while len(pq1) < candidates and i <= j: # pq1의 길이가 후보 수보다 작고, i가 j 이하이면
                heapq.heappush(pq1, costs[i]) # pq1에 costs[i]를 heappush하고
                i += 1 # i를 1 증가
            while len(pq2) < candidates and i <= j: # pq2의 길이가 후보 수보다 작고, i가 j 이하이면
                heapq.heappush(pq2, costs[j]) # pq2에 costs[j]를 heappush하고
                j -= 1 # j를 1 감소
            
            t1 = pq1[0] if pq1 else float('inf') # pq1의 첫번째 값(최소값)이 음의 무한대가 아니고, 실제로 존재하면 해당 값 할당
            t2 = pq2[0] if pq2 else float('inf') # pq2의 첫번째 값(최소값)이 음의 무한대가 아니고, 실제로 존재하면 해당 값 할당

            if t1 <= t2: # t1보다 t2가 더 큰 경우,
                res += t1 # res에 t1을 더하고
                heapq.heappop(pq1) # pq1에서 heappop
            else: # t2보다 t1가 더 큰 경우, 
                res += t2 # res에 t2을 더하고
                heapq.heappop(pq2) # pq2에서 heappop
            # k를 1 감소
            k -= 1
        # 최종 res 반환
        return res