class Solution:
    def maxDepth(self, s: str) -> int:
        maxcount = 0
        cnt = 0

        for i in s:
            if i == "(":
                cnt += 1
            if i == ")":
                cnt -= 1
            if (cnt >= maxcount):
                maxcount = cnt
        
        return maxcount
    
"""
Runtime 51 ms
Memory 16.3 MB
"""