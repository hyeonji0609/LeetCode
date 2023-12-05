class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        MaxAltitude = 0
        iAltitude = MaxAltitude

        for i in gain:
            iAltitude = iAltitude + i
            if iAltitude > MaxAltitude:
                MaxAltitude = iAltitude

        return MaxAltitude
    
    """
    Rumtime 29 ms
    Memory 16.3 MB
    """