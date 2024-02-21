# Ver.1
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countarr = []
        
        for i in set(arr):
            counti = arr.count(i)
            if counti in countarr:
                return False
            else:
                countarr.append(counti)
        
        return True

"""
Runtime 43 ms
Memory 16.56 MB
"""

# Ver.2
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hasharr = dict()

        for i in set(arr):
            hasharr[i] = arr.count(i)

        return len(set(hasharr.values())) == len(hasharr.values())

"""
Runtime 57 ms
Memory 16.75 MB
"""