class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 전체 합 계산
        total_sum = sum(nums)
        # 왼쪽 합 초기화
        left_sum = 0

        # for 루프로 업데이트
        for i in range(len(nums)):
            # 첫번째 값이 아닐때에만 업데이트
            if i != 0:
                left_sum += nums[i-1]
            # 오른쪽 합 = 전체 합 - 현재값 - 왼쪽합
            right_sum = total_sum - nums[i] - left_sum

            # 왼쪽 합과 오른쪽 합이 같으면 현재 index 반환
            if left_sum == right_sum:
                return i

        # 아니면 False 반환
        return -1
    
'''
Runtime 141ms - Beats 51.25%
Memory 17.59MB - Beats 50.00%
'''