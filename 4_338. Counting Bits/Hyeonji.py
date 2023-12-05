class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i)[2:].count('1') for i in range(n+1)]
        # bin 함수를 이용하여 문자열에서 1의 갯수 세기
        # [2:]는 bin함수를 쓰게 되면 리턴값으로 '0b'가 붙기때문에 제거해주기 위함

"""
Runtime: 82 ms
Memory Usage: 23.1 MB
"""