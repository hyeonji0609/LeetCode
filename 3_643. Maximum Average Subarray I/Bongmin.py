class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 리스트의 길이와 k가 같다면 그대로 나눠주고 리턴
        if len(nums) == k:
            return sum(nums) / k
        # 다르다면
        else:
            ls = []
            first = sum(nums[:k]) # 초기값을 지정해주고 (처음 k개 만큼 자른 합)
            ls.append(first)
            for i in range(len(nums)-k):
                first -= nums[i] # 처음 것을 빼고
                first += nums[i+k] # 마지막을 추가함 
                ls.append(first)
            return max(ls)/k

'''
runtime : 999 ms beats 77.64!
memory : 28.4 mb 
'''