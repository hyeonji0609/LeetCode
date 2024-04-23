class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # start(최소속도 k는 1로 시작)
        start = 1
        # end는(최대속도 k) 바나나 더미 중 가장 큰 값
        end = max(piles)
        # 각 더미에서 주어진 속도 k로 바나나를 먹는 데 필요한 시간을 계산하는 함수
        def canEatAll(piles, k, h):
            total_time = 0 # 먹는데 걸린 총 시간
            # 각 바나나 더미 루프
            for pile in piles:
                # 시간 당 먹을 수 있는 바나나 수는 k
                # 바나나 더미가 k로 안나눠지면 시간을 1 추가해줘야 함
                total_time += (pile + k - 1) // k  # 올림 연산(x + n - 1) // n은 항상 올림 연산임.
            return total_time <= h # 먹는데 걸린 총 시간이 h이하인 경우
        
        # 최소속도 k를 찾을 때까지 반복
        while start < end:
            # mid(속도 k) 계산
            mid = (start + end) // 2
            if canEatAll(piles, mid, h): # 먹는데 걸린 총 시간이 h이하인 경우
                end = mid  # end=mid로 업데이트해서, 속도를 더 낮출 수 있음.
            else:
                start = mid + 1  # 그렇지 않으면, 속도를 더 높혀야 함.

        return start  # 최소 속도 반환
    
    '''
    Runtime 252 ms - Beats 87.75%
    Memory 18.00 MB - Beats 99.04%
    '''