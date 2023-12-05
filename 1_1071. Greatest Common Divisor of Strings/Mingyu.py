import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 두 문자열 길이 변수 생성
        len1, len2 = len(str1), len(str2)
        # math 함수로 개건방지게 최대공약수 구하기
        gcd = math.gcd(len1, len2)
        # 둘 중에 아무 문자열에서 최대공약수만큼의 부분 문자열 생성
        gcd_string = str1[:gcd]

        # 두 문자열이 부분문자열을 곱해서 생성할 수 있다면 부분문자열 반환
        if str1 == gcd_string * (len1//gcd) and str2 == gcd_string * (len2//gcd):
            return gcd_string
        # 아니면 빈 문자열 반환
        else:
            return ""
        
'''
Runtime 44ms - Beats 32.10%
Memory 16.29MB - Beats 52.46%
'''