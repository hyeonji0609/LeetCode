class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [candy + extraCandies >= max_candies for candy in candies]
        return result


'''
Runtime : 35 ms : beats 94.23%
Memory : 17.35 : beats 16.91%
'''