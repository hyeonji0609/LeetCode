class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s_list = list(s)
        temp_list = []
        result_list = []

        while s_list != []:
            temp_list.append(s_list.pop())
            if temp_list.count("(") == temp_list.count(")"):
                temp_list.pop()
                temp_list.reverse()
                temp_list.pop()
                while temp_list != []:
                    result_list.append(temp_list.pop())
        
        result_list.reverse()
        result = "".join(result_list)
        return result
    
"""
Runtime 53 ms
Memory 16.49 MB
"""