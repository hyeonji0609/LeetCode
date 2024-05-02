class Solution:
    def tribonacci(self, n: int) -> int:
        # Tabulation 풀이
        trib = [0, 1, 1] # trib(0)=0, trib(1)=1, trib(2)=1
        for i in range(3, n+1):
            trib.append(trib[i-3] + trib[i-2] + trib[i-1])
        return trib[n]
    '''
    Runtime 34 ms - Beats 58.45%
    Memory 16.56 MB - Beats 32.50%
    '''