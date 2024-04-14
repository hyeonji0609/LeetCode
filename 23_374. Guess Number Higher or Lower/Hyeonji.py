class Solution:
    def guessNumber(self, n: int) -> int:
        start = 1
        end = n
        
        if guess(n) == 0:
            return n
        
        while start <= end:
            mid = (start+end) // 2
            
            if guess(mid) == -1 : # mid가 pick보다 높은 경우
                end = mid
            elif guess(mid) == 1 : # mid가 pick보다 낮은 경우
                start = mid
            elif guess(mid) == 0:
                return mid

"""
Runtime: 36 ms
Memory Usage: 16.5 MB
"""