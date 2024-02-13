import heapq

def solution(scoville, K):
    answer = 0
    # 1. scoville을 최소힙 정렬 수행
    heapq.heapify(scoville)
    # 2. scoville의 모든 요소가 K 이상일 때 까지 루프
    while scoville[0] < K:
        # 3. 만약 scoville의 길이가 1이고, scoville[0] < K이면, 모든 요소를 K 이상으로 만들 수 없으므로 -1 return
        if len(scoville) < 2:
            return -1
        # 4. 가장 작은 값과 두번째로 작은 값을 토대로 scoville 배열 업데이트 및 업데이트 횟수 카운트
        mildest = heapq.heappop(scoville)
        second_mildest = heapq.heappop(scoville)
        heapq.heappush(scoville, (mildest + 2 * second_mildest))
        answer += 1

    return answer