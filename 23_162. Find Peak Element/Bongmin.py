class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: # 길이가 1이라면 자기 index가 0번째이므로 0리턴
            return 0
        # 길이가 2이상일때 
        for i in range(len(nums)):
            # 인덱스 i가 맨 끝이라면 이때까지 peak가 없었다는 뜻
            if i == len(nums)-1:
                # 맨 끝의 인덱스 i와 그 전 값인 i-1의 값을 비교하여 큰거 리턴
                return i if nums[i]>nums[i-1] else i-1
            # 그게 아니라면 중간 인덱스를 리턴
            elif (nums[i-1] < nums[i]) & (nums[i+1] < nums[i]):
                return i
            
'''
runtime : 53ms / 15.12%
memory : 16.74mb / 37%
'''