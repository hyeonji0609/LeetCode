import heapq

def solution(scoville, K):
    # scoville 최소 힙 만들기
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    # 섞은 횟수
    mix_count = 0
    
    while heap:
        min_val = heapq.heappop(heap) # 최소 값
        # 꺼내자마자 K보다 크면 break
        if min_val >= K:
            break
        # 힙이 비면 -1
        if not heap:
            return -1
        # 두 번째 작은 값
        second_min_val = heapq.heappop(heap)
        # new 스코빌 계산하기
        new_val = min_val + (second_min_val * 2)
        # new 스코빌을 heap에 추가
        heapq.heappush(heap, new_val)
        # 섞은 횟수 추가
        mix_count += 1
    # heap을 다 돌았다면 count를 반환하기
    return mix_count
    