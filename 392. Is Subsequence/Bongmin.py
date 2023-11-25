class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        try:
            for i in s:
                if i not in t:
                    raise
            for i in range(len(s)-1):
                if t.index(s[i]) > t.index(s[i+1]):
                    raise
                
            return True
        except:
            return False



