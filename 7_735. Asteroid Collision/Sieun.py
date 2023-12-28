class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            while stack and stack[-1] > 0 and i < 0:
                abs_i = abs(i)
                if stack[-1] < abs_i:
                    stack.pop()
                    continue
                elif stack[-1] == abs_i:
                    stack.pop()
                break
            else:
                stack.append(i)
        
        return stack

"""

"""
