class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # nums를 오름차순 정렬
        sorted_nums = sorted(nums)
        # 정렬한 리스트에서 start와 end 초기 인덱스 설정
        start , end = 0, len(sorted_nums) - 1
        # 정렬한 리스트에서 target을 nums의 최댓값으로 설정
        target = max(sorted_nums)

        while start <= end: # 이진탐색 구현
            mid = (start + end) // 2

            if sorted_nums[mid] == target:
                # 찾은 값을 원본 리스트의 인덱스로 반환
                return nums.index(sorted_nums[mid])
            elif sorted_nums[mid] < target:
                start = mid + 1
            elif sorted_nums[mid] > target:
                end = mid - 1
'''
Runtime 49 ms - Beats 40.09%
Memory 16.75 MB - Beats 37.51%
'''