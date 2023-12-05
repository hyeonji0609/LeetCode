class Solution:
    def reverseVowels(self, s: str) -> str:
        ls = [x for x in s] # input str 리스트화
        vowels = ['a','e','i','o','u',"A","E","I","O","U"] # 모음 목록

        # ls에 들어가있는 모음만 추출
        ls_vowels = [] 
        for i in ls:
            if i in vowels:
                ls_vowels.append(i)

        ls_vowels.reverse() # 뒤집기

        n = 0
        cor = ""
        for i in range(len(ls)):
            if ls[i] in vowels:
                cor += ls_vowels[n]
                n+=1
            else:
                cor += ls[i]
        return cor

'''
runtime : 74 ms
memory : 18 mb
'''