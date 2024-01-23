class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = list(range(1, n+1))
        idx = 0

        while len(circle) > 1:
            idx = (idx + k - 1) % len(circle)
            del circle[idx]
        
        return circle[0]

"""
Runtime 39 ms
Memory 16.69 MB
"""