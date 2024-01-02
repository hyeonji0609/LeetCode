class Solution:
    def removeStars(self, s: str) -> str:
        # * 앞에 문자를 추척할 스택 생성
        stack = []

        for char in s:
            # 문자가 '*'이 아니면 stack에 추가
            if char != '*':
                stack.append(char)
            # stack이 비어있지 않다면,
            elif stack:
                # stack의 마지막 요소 제거('*' 바로 앞에 문자)
                stack.pop()
        return ''.join(stack) # stack의 구성 요소들을 join하여 문자열로 return('*'과 그 앞에 문자는 없음)
    
    '''
    Runtime 266ms - Beats 25.52%
    Memory 19.04MB - Beats 9.84%
    '''