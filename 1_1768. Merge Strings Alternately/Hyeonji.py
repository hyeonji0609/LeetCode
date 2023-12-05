class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        result = []

        if len_word1 >= len_word2:
            for i in range(len_word2):
                result.append(word1[i])
                result.append(word2[i])

            result.append(word1[len_word2:])
        
        else :
            for i in range(len_word1):
                result.append(word1[i])
                result.append(word2[i])

            result.append(word2[len_word1:])

        result = "".join(result)

        return result
    
"""
Runtime 38 ms
Memory 	16.1 MB
"""