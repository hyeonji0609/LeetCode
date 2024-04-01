class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # 재귀 함수 정의
        def circular_game(n, k):
            # 한명만 남으면 그 사람의 인덱스는 0이므로 0을 리턴
            if n == 1:
                return 0
            # 그렇지 않으면,
            else:
                # (이전 승자의 위치 + k) % 현재 남은 인원수 (모듈러 연산)
                # 
                return (circular_game(n -1, k) + k) % n
        # 0부터 시작하므로 1을 더해서 리턴
        return circular_game(n, k) + 1
    '''
    Runtime 42 ms - Beats 51.26%
    Memory 16.66 MB - Beats 37.25%
    '''