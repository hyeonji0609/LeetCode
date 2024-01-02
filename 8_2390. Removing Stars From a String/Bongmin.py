# 별 지우고, 별 바 왼쪽도 지우고
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)
            elif i == "*":
                stack.pop()
        return "".join(stack)
    
    
'''
Runtime : 294 ms
memory : 19.1 mb
'''