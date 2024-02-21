# Ver.1
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        countword1 = [word1.count(i) for i in set(word1)]
        countword2 = [word2.count(j) for j in set(word2)]

        return sorted(countword1) == sorted(countword2)

"""
Runtime 91 ms
Memory 17.83 MB
"""

# Ver.2
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False
        
        countword1 = {i: word1.count(i) for i in set(word1)}
        countword2 = {j: word2.count(j) for j in set(word2)}

        return sorted(countword1.values()) == sorted(countword2.values())

"""
Runtime 82 ms
Memory 17.94 MB
"""