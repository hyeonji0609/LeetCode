stack = []
result = []

for i in list(s):
    if i == ']' :
        bracket = []

        for j in stack[::-1] :
            if j != '[' :
                bracket.append(stack.pop())
            else :
                break

        stack.pop()
        bracket.append(stack.pop())
        result.append(int(bracket[::-1][0]) * str(''.join(bracket[::-1][1:])))
        result.append(stack.pop())

#         for k in stack :
#             if k != '[':
#                 result.append(stack.pop())
#             else :
#                 break
#         result.append(int(bracket[::-1][0]) * str(''.join(bracket[::-1][1:])))

        else :
            stack.append(i)

"""
"""