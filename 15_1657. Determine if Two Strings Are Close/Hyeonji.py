class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) == len(word2):
            word1_ = set(word1)
            word2_ = set(word2)

            count1 = [word1.count(i) for i in word1_]
            count2 = [word2.count(i) for i in word2_]

            operation_1 = len(word1_.difference(word2_))
            operation_2 = (sorted(count1) == sorted(count2))

            if operation_1 == 0:
                if operation_2 == 1 :
                    return True
        else:
            return False

"""
Runtime: 78 ms
Memory Usage: 17.7 MB
"""