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
Runtime : 294 ms 상위 80%..?
memory : 19.1 mb 상위 5%
런타임도 안좋고 메모리도 안좋다 2
'''