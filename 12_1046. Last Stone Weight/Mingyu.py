import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 돌에 -1 곱해서 stones 재구성
        stones = [-stone for stone in stones]
        # heapify로 최대힙 구현
        heapq.heapify(stones)
    
        # 돌이 1개 이상일 때 까지만 루프
        while len(stones) > 1:
            # 가장 무거운돌과 두번째로 무거운돌 할당 및 - 곱해서 무게 변환
            heaviest = -heapq.heappop(stones)
            second_heaviest = -heapq.heappop(stones)

            # 만약 두 무게가 다르면 둘을 빼준 후 -1 곱해서 최대힙에 재할당
            if heaviest != second_heaviest:
                heapq.heappush(stones, -(heaviest - second_heaviest))

        # while 루프 종료 후 stones에 값이 있으면 -곱해서 리턴
        if stones:
            return -stones[0]
        # 그렇지 않으면 0 리턴
        else:
            return 0
        
        '''
        Runtime 42 ms - Beats 32.75%
        Memory 16.52 MB - Beats 62.22%
        '''