class Solution:
    def tribonacci(self, n: int) -> int:
        # memoization을 위한 배열 선언
        tribodata = [0] * (n+1)
        tribodata[1:3] = [1, 1] # 2 이하에 1 삽입
        
        def tribo(n, data):
            if data[n] != 0:
                return data[n]
            if n <= 1:
                return data[n]
            else:
                data[n] = tribo(n-1, data) + tribo(n-2, data) + tribo(n-3, data)
                return data[n]
        
        return tribo(n, tribodata)

"""
Runtime: 45 ms
Memory Usage: 16.5 MB
"""