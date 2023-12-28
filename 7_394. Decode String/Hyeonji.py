s = "2[abc]3[cd]ef"

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
        stack.append(int(bracket[::-1][0]) * str(''.join(bracket[::-1][1:])))

    else :
        stack.append(i)
print(''.join(result))
