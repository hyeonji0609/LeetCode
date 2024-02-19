class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # 두 리스트의 값을 추적할 딕셔너리 생성
        dict1, dict2 = {}, {}
        # word1의 단어의 등장 횟수를 dict1에 할당
        for char in word1:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        # word2의 단어의 등장 횟수를 dict2에 할당
        for char in word2:
            if char in dict2:
                dict2[char] += 1
            else:
                dict2[char] = 1
        
        # 두 문자열에 등장하는 문자 집합이 같은지 확인
        if set(dict1.keys()) != set(dict2.keys()):
            return False
        
        # 두 문자열에서 각 문자의 등장 횟수 리스트를 오름차순 정렬하여 비교
        if sorted(dict1.values()) == sorted(dict2.values()):
            return True
        else:
            return False
        
        '''
        Runtime 226 ms - Beats 12.79%
        Memory 17.26 MB - Beats 99.92%
        '''