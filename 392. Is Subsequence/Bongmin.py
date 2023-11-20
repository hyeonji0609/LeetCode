class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return "false"
                break
        for i in range(len(s)-1):
            if t.index(s[i]) > t.index(s[i+1]):
                return "false"
                break
        return "true"