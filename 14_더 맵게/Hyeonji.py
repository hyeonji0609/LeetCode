import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    minimum = heapq.heappop(scoville)
    answer = 0
    
    if minimum >= K : # 처음 뽑은 최솟값이 K보다 크면
        return answer # 바로 리턴
    
    while (minimum < K) : # 아니면 K가 작을 때 까지 반복
        if minimum >= K : # 최솟값이 K보다 크면 리턴
            return answer
        if len(scoville) == 0 and minimum <= K : # 만약 리스트에 값이 없고, 최솟값이 K보다 작으면
            return -1 # -1 리턴
        
        minimum_2nd = heapq.heappop(scoville) # 두 번째로 맵지 않은 스코빌
        mix_scoville = minimum + (minimum_2nd * 2) # 섞은 음식의 스코빌
        heapq.heappush(scoville, mix_scoville) # 다시 힙에 넣어주기
        answer += 1 # 횟수 갱신

        minimum = heapq.heappop(scoville) # 최솟값 갱신

    return answer