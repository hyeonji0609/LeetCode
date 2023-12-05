class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max([0]+[sum(gain[:i+1]) for i in range(len(gain))])

"""
Runtime: 40 ms
Memory Usage: 16.4 MB
"""        