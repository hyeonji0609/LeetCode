class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {} # dict 형태
        for i in nums: # nums를 받아와서 
            if i in counts: # 카운트dict에 있다면 
                counts[i] += 1 # 하나 
            else: # 없다면
                counts[i] = 1 # 그 숫자를 하나 추가

        for num, count in counts.items(): # dict에 items를 받아와서
            if count == 1: # 한개짜리 
                return num # 리턴

'''
RunTime : 119 ms
Memory : 19.1 mb
'''