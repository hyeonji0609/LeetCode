class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_arr = set(arr)
        number = []
        
        for i in unique_arr:
            number.append(arr.count(i))
        
        if len(set(number)) == len(number):
            return True
        else:
            return False
"""
Runtime: 42 ms
Memory Usage: 16.6 MB
"""