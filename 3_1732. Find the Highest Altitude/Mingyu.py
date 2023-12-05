class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        altitude_list = [0]
        for i in range(len(gain)):
            altitude += gain[i]
            altitude_list.append(altitude)
        return max(altitude_list)
    
'''
Runtime 44ms - Beats 42.11%
Memory 16.33MB - Beats 9.36%
'''