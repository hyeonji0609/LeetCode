import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) > 1 and scoville[0] < K:
        min_scv = heapq.heappop(scoville)
        min_second_scv = heapq.heappop(scoville)
        new_scv = min_scv + (min_second_scv * 2)
        heapq.heappush(scoville, new_scv)
        answer += 1

    if scoville[0] < K:
        return -1
    else:    
        return answer