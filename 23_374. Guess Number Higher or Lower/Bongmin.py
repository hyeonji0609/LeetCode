# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1 # 시작
        end = n # 끝
        while start<=end:
            mid = (start + end) // 2
            if guess(mid) == 1: # 높여라 -> start를 높여서 new_mid를 높여라
                start = mid + 1
            elif guess(mid) == -1: # 낮춰라 -> end를 낮춰서 new_mid를 낮춰라
                end = mid - 1 
            elif guess(mid) == 0: # 맞췄다
                return mid
        return None
'''
runtime : 39ms / beats : 23%
memory : 16.5mb / beats : 15.11%
'''

