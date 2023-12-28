class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        stack.append(asteroids[0])

        for i in range(1, len(asteroids)) :
            stack.append(asteroids[i])

            first = stack.pop()
            second = stack.pop()

            if first < 0 and second > 0 :
                if abs(first) != abs(second) :
                    stack.append(first if abs(first)> abs(second) else second)
            else :
                stack.append(second)
                stack.append(first)
                print(f"else asteroids : {asteroids}")

"""
미해결 : [10, 2, -5] 할 때 마지막 비교가 안됨....
[10, -5]에서 for문이 종료되어버림 ㅠㅠ
1. while문 써야함
"""