from heapq import heappush, heappop
from operator import itemgetter

class Solution:
    def maxScore(self, nums1, nums2, k):
        # 초기 최대 점수와 누적 합계를 0으로 설정, 최소 힙 초기화
        highestScore, cumulativeSum, heap = 0, 0, []
        
        # nums1과 nums2 원소들을 쌍으로 묶고, nums2 기준으로 내림차순 정렬
        pairs = sorted(zip(nums1, nums2), key=itemgetter(1), reverse=True)
        
        for num1, num2 in pairs:
            # nums1에서 원소들의 누적 합 업데이트
            cumulativeSum += num1
            # 해당 원소를 최소 힙에 추가
            heappush(heap, num1)
            
            # 힙의 크기가 k를 초과하면, 가장 작은 원소 제거 후 누적 합에서 차감
            if len(heap) > k:
                cumulativeSum -= heappop(heap)
            
            # 힙의 크기가 k에 도달하면, 현재 누적 합과 nums2의 원소를 곱해 최대 점수 갱신
            if len(heap) == k:
                highestScore = max(highestScore, cumulativeSum * num2)
        
        return highestScore