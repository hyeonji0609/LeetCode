class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        brackets = []
        output = []
        open_bracket = 0
        idx = 0
        
        for i, bracket in enumerate(s):
            if bracket == '(': # 왼쪽 괄호만큼 갯수 세기
                open_bracket += 1
            elif bracket == ')': # 오른쪽 괄호만큼 갯수 세기
                open_bracket -= 1
            
            if open_bracket == 0 : # 만약 오른쪽 괄호와 왼쪽 괄호 갯수가 같으면?
                brackets.append(s[idx:i+1]) # 리스트 슬라이싱 해서 그부분만 넣어주기
                idx = i+1
        
        for i in brackets :
            output.append(i[1:-1]) # 맨 가쪽 괄호만 없애기
        
        return ''.join(output)
        
"""
Runtime: 56 ms
Memory Usage: 16.6 MB
""" 
            
            
        
                
                