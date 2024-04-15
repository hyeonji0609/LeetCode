class Solution:
    def guessNumber(self, n: int) -> int:
        # start는 1로, end는 n으로
        start = 1
        end = n
        # start가 end 이하일 때까지 루프
        while start <= end:
            # mid는 start + end는 둘의 중간 값으로 지정
            mid = (start + end) // 2
            # guess(mid)의 결과가 0이면(mid==target), mid를 반환
            if guess(mid) == 0:
                return mid
            # guess(mid)의 결과가 1이면(mid<target), start= mid + 1
            elif guess(mid) == 1:
                start = mid + 1
            # guess(mid)의 결과가 -1이면(mid>target), end = mid - 1
            elif guess(mid) == -1:
                end = mid - 1
'''
Runtime 30 ms - Beats 83.21%
Memory 16.48 MB - Beats 67.67%
'''