class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        if len(s) == 0 : # s가 ""인 경우 무조건 True
            return True
        elif len(t) == 0 : # t가 ""인 경우 무조건 False
            return False
        
        for i in s :
            if i in t :
                t_idx = t.index(i) # t에 s인자가 있다면 가장 첫번째 인덱스를 반환
                t = t[t_idx+1:] # 처음으로 찾은 값 제외하고 찾게끔 슬라이싱
                output = True
                continue
            else:
                output = False # t에 s인자가 없다면 false 반환
                break
        
        return output

"""
Runtime: 50 ms
Memory Usage: 16.4 MB
"""