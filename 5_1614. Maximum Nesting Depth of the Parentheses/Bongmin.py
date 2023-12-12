'''
idea
괄호를 열었을 때 마다 카운트를 +1 해주고 
result보다 열려져있는 것이 많다면 교체
'''

class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        result = 0
        
        for i in s:
            if i == "(": # 열었을 때 
                count += 1 # +1 해주고
                if count > result: # count보다 result가 크다면
                    result = count # 교체
                
            elif i == ")": # 닫았을 때는
                count -= 1 # -1

        return result


'''
Runtime : 34 ms
Memory : 16.3 MB
'''