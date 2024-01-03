class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        s_list = list(s)

        for i in s_list :
            stack.append(i) # for문을 돌 때 마다 stack에 저장

            if i == '*' : # 만약 *을 만나면
                stack.pop() # *을 우선적으로 pop하고
                stack.pop() # * 바로 앞의 값도 stack에서 pop
        
        return ''.join(stack)

"""
Runtime: 172 ms
Memory Usage: 19.6 MB
"""