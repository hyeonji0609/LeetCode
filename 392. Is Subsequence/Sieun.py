# Solution 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        next_loop_idx = 0
        char_list = []
        result = False
        
        if s == "":
            result = True
        else:
            if t == "":
                result = False
            else:
                for i in range(len(s)):
                    for j in range(next_loop_idx, len(t)):
                        if s[i] == t[j]:
                            next_loop_idx = j+1
                            char_list.append(s[i])
                            break

        if "".join(char_list) == s:
            result = True
                    
        return result

"""
Runtime 36ms
Memory 16.44MB
"""

# Solution 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        result = True

        for i in s:
            if t.find(i) == -1:
                result = False             
            else:
                t = t[t.find(i)+1:]

        return result
    
"""
Runtime 36ms
Memory 16.44MB
"""

# 왜 두 Solution의 메모리 값이 같은지?