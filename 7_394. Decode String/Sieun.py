class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in s:
            if i.isdigit( ):
                if stack and stack[-1].isdigit():
                    stack[-1] += i
                else:
                    stack.append(i)
            elif i == "[" or i.isalpha():
                stack.append(i)
            elif i == "]":
                temp_str = ""
                while stack and stack[-1] != '[':
                    temp_str = stack.pop() + temp_str
                stack.pop()
                k = int(stack.pop())
                stack.append(temp_str * k)

        return ''.join(stack)
