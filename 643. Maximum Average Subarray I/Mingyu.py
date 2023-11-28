class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 처음 k까지의 합 계산
        current_sum = sum(nums[:k])
        # 처음 평균 계산
        max_avg = current_sum / k

        # for 루프로 업데이트
        for i in range(k, len(nums)):
            # 처음 k까지의 합에서 맨 왼쪽 값을 빼고 다음 값 더하기
            current_sum += nums[i] - nums[i-k]
            # 최대 평균 업데이트
            max_avg = max(max_avg, current_sum / k)

        return max_avg
    
'''
Runtime 997ms - Beats 79.81%
Memory 27.84MB - Beats 83.41%
'''