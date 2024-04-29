class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digits이 비어있으면 빈 리스트 반환
        if not digits:
            return []
        
        # 숫자와 문자 사전 정의
        digit_char_info = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        # result를 리스트로 초기화
        result = [] 

        # backtrack 함수 정의
        # 인자 : (현재 처리중인 digit 인덱스, 현재까지 만든 문자 조합)
        def backtrack(index, current_comb):
            if index == len(digits): # 현재 index가 digits의 길이와 같으면
                result.append(current_comb) # 여태 만든 조합을 모두 result에 할당 후 종료
                return
            # current_digit에 현재 digits의 index 할당
            current_digit = digits[index]
            # 사전에 정의한 사전에서 해당 숫자에 해당하는 문자열 루프
            for char in digit_char_info[current_digit]:
                # 다음에 처리할 digit과 현재까지의 문자 조합에 현재 digit에 해당하는 문자 중 하나를 추가
                backtrack(index + 1, current_comb + char)
        # 0번 인덱스와 빈 문자열부터 시작
        backtrack(0, "")

        return result
    '''
    Runtime 39 ms - Beats 26.88%
    Memory 16.5 MB - Beats 89.34%
    '''