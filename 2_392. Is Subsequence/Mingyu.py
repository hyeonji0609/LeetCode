class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list, t_list = list(s), list(t)
        correct_count = 0
        
        # s가 빈 문자열이면 True 반환
        if len(s_list) ==0:
                return True

        for i in range(len(t_list)): # s[correct_count]와 t_list[i]가 같으면 correct_count 1 증가
            if s_list[correct_count] == t_list[i]:
                correct_count +=1
                if correct_count == len(s_list): # s 안에 있는 모든 문자를 찾았으면 True 
                    return True

        return False # 그렇지 않으면 False
    
'''
Runtime 29ms - Beats 97.41%
Memory 16.46MB - Beats 7.51%
'''