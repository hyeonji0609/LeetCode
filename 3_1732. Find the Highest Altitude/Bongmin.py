class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain = [0] + gain
        ls = []
        n= 0
        for i in gain:
            n += i
            ls.append(n)
        return max(ls)
    
'''
Runtime : 41 ms
Memory : 16.24 mb
'''