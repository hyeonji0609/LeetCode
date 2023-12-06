# stack을 공부하고 풀어보자!

# ( ( ) ( ) ) ( ( ) ) 
# 1 2 1 2 1 0 1 2 1 0
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        count = 0

        for i in s:
            if i == "(": # 여는 경우.
                if count > 0: # count가 0보다 크다면 --> 0보다 커야 맨 앞의 여는 괄호 제거 가능
                    result += i # "(" 하나 추가
                count +=1 # 카운트 하나 추가
            
            elif i == ")": # 닫는 경우 
                count -=1 # 카운트 하나 제거를 먼저 해야 마지막 닫는 괄호 포함 X
                if count > 0 : # 마찬가지로 count가 0보다 커야 맨 뒤의 닫는 괄호 제거 가능
                    result += i # ")" 하나 추가
                
        return result

'''
Rentime : 47ms
Memory : 16.3mb
'''

# stack으로 쓰려나 어떻게 써야할 지 모르겠어서 이렇게 풀었습니다 ㅠㅠ