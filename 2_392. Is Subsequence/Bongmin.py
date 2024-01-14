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


###########
# 오답노트
###########
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        cnt = len(s)
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        if cnt == i:
            return True
        else:
            return False
'''
runtime : 35ms : beats 79.57%
memory : 17.34MB : beats 29.95%
'''
