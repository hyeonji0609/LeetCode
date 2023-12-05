class Solution:
    def reverseVowels(self, s: str) -> str:
        aeiou = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        idx_list = []
        s_list = list(s)  # 문자열에서는 인덱스 교환을 통한 위치 교환이 불가능함

        for i in range(len(s)):
            if s[i] in aeiou:
                idx_list.append(i)
        
        if idx_list != 0:
            for j in range(len(idx_list)//2):
                s_list[idx_list[j]], s_list[idx_list[-j-1]] = s_list[idx_list[-j-1]], s_list[idx_list[j]]

        result = ''.join(s_list)

        return result
    
    """
    Runtime 59ms
    Memory 18.7MB
    """