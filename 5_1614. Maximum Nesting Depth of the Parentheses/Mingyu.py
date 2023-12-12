class Solution:
    def maxDepth(self, s: str) -> int:
        # "("를 추적할 스택 생성
        stack = []
        # 최대 깊이 초기화
        max_depth = 0

        # 문자열 내의 각 문자를 순회
        for char in s:
            # 문자열이 "("이면 stack에 추가
            if char == '(':
                stack.append(char)
                # 현재 max_depth와 stack의 크기를 비교하여 더 큰 값을 max_depth로 업데이트
                max_depth = max(max_depth, len(stack))
            
            # 문자열이 ")"이면 stack에서 "("제거
            elif char == ')':
                stack.pop()

        return max_depth
    
'''
Runtime 35 ms - Beats 76.7%
Memory 16.2 MB - Beats 79%
'''