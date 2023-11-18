class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = set('aeiouAEIOU') # 모음집합 정의
        s_list = list(s) # 문자열 리스트로 변환
        # 2개의 포인터인 시작 인덱스와 마지막 인덱스 정의
        i = 0
        j = len(s_list)-1 

        while i < j: # j가 i보다 클때까지만 진행
            # i,j가 모두 모음집합에 속하면 자리 변환하고 i는 1 증가 j는 1 감소
            if s_list[i] in vowel_set and s_list[j] in vowel_set:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1

            # i가 모음 집합에 없으면 i는 1 증가
            elif s_list[i] not in vowel_set:
                i += 1
            # j가 모음 집합에 없으면 j는 1 증가
            elif s_list[j] not in vowel_set:
                j -= 1
        # 변경된 리스트 결과를 문자열로 변환
        s = ''.join(s_list)

        return s
    
'''
Runtime 50ms - Beats 81.84%
Memory 7.40MB - Beats 55.36%
'''