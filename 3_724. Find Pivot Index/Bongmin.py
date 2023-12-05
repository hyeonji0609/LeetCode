class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = 0 # 인덱스를 저장할 초기값
        for i in range(len(nums)): # 리스트를 돌아서
            if sum(nums[:i]) == sum(nums[i+1:]): # 양쪽으로 나눈 것들의 합이 같으면
                n = i # 그 인덱스를 반환
                break
            else:
                n = -1 # 없으면 -1
        return n
'''
runtime : 6595 ms
memory : 17.5 mb
'''