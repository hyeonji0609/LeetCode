# 별 바로 왼쪽 지우고 별도 지우고
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i != "*":
                stack.append(i)
            elif i == "*":
                stack.pop()
        return "".join(stack)