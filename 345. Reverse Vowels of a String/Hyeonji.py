class Solution:
    def reverseVowels(self, s: str) -> str:
        list_s = list(s)
        
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        vowel_idxs = []
        vowel_values = []
        
        for idx in range(len(list_s)) :
            if list_s[idx] in vowel :
                vowel_idxs.append(idx) # 모음인 값의 인덱스 추가
                vowel_values.append(list_s[idx]) # 모음 값 추가 
        
        vowel_idxs.reverse() # 인덱스만 뒤집기
        
        for i in range(len(vowel_idxs)) : # 모음 값을 인덱스를 뒤집어서 재할당
            list_s[vowel_idxs[i]] = vowel_values[i] 
        
        return ''.join(list_s)

"""
Runtime: 47 ms
Memory Usage: 18.9 MB
"""