from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(digits) # 숫자를 하나하나 쪼개기
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        number = []
        
        for num in digits:
            number.append(letters[int(num)-2]) # digit가 2부터 시작하는데, letters 인덱스는 0부터 시작하므로 -2
        
        return [''.join(x) for x in product(*number)] if len(digits) != 0 else []
    
"""
Runtime: 29 ms
Memory Usage: 16.5 MB
"""

"""
product
- 중복 순열 내장함수
- 리스트가 2개 이상 들어가면 가능한 모든 조합을 구해준다
"""
