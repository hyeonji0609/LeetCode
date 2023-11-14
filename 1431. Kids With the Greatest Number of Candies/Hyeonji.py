class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        output = []

        for i in candies:
            greatest = i + extraCandies
            if greatest >= max_candy:
                output.append(True)
            else:
                output.append(False)
        
        return output

"""
Runtime: 43 ms
Memory Usage: 16.1 MB
"""