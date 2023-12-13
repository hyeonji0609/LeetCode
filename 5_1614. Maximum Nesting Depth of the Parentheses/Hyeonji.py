class Solution:
    def maxDepth(self, s: str) -> int:
        paren = []
        paren_num = 0
        
        if '(' in s or ')' in s :
            for i in list(s):
                if i == '(' :
                    paren_num += 1
                    paren.append(paren_num) # 오른쪽 괄호가 있을때마다 count
                elif i == ')' :
                    paren_num -= 1
            return max(paren) # 최대 오른쪽 괄호 갯수 return
        else :
            return 0

"""
Runtime: 49 ms
Memory Usage: 16.3 MB
"""