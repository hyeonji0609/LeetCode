class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 빈 리스트면 빈 값
        if not digits:
            return []
        nums_alpha = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # 결과
        res = []
        def back(text, digits):
            # 남은 숫자가 없다면 그 문자를 넣고 종료
            if not digits:
                res.append(text)
                return
            # 남은 숫자의 1번째 값에 해당하는 alpha들 가져오기
            for alpha in nums_alpha[digits[0]]:
                # text에 들어온 alpha를 추가하고 숫자도 한칸 띄어 넣기
                back(text + alpha, digits[1:])

        back('', digits)
        return res
    
"""
runtime : 36ms / 50.41%
memory : 16.5 / 89.38%
"""