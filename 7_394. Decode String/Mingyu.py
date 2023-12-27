class Solution:
    def decodeString(self, s: str) -> str:
        # "["를 추적할 스택 생성
        stack = []
        # 현재 반복 횟수
        current_num = 0
        # 현재까지 추적한 문자열
        current_str = ""

        # 문자열 내의 각 문자를 순회
        for char in s:
            # 문자가 숫자인 경우에 자릿수를 고려해서 int형으로 current_num에 할당
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            # '['인 경우에 
            elif char == '[':
                # stack에 tuple로 (이전에 저장된 문자열, 현재 반복횟수) 저장
                stack.append((current_str, current_num))
                # 현재까지 추적한 문자열과 반복횟수 초기화
                current_str, current_num = "", 0
            # ']'인 경우에 
            elif char == ']':
                # stack에 저장된 tuple을 추출
                prev_str, num = stack.pop()
                # 현재 문자열을 이전 문자열 + (반복횟수) * 현재 문자열로 결합하여 업데이트
                current_str = prev_str + current_str * num
            # 문자가 숫자나 괄호가 아닌 경우에
            else:
                # 현재 문자열에 추가
                current_str += char
        return current_str

# 숫자 반복 예시 100[leetcode]
# 첫번째 숫자 1: current_num * 10 + int(char) -> 0(초기값) * 10 + 1 = 1
# 두번째 숫자 0: current_num * 10 + int(char) -> 1(업데이트) * 10 + 0 = 10
# 세번째 숫자 0: current_num * 10 + int(char) -> 10(업데이트) * 10 + 0 = 100

'''
Runtime 33ms - Beats 84.04%
Memory 17.19MB - Beats 6.32%
'''