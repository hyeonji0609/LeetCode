class Solution:
    def countBits(self, n: int) -> List[int]:
        bits_list = []
        for i in range(n+1):
            bits_list.append(list(bin(i)[2:]).count('1'))
        return bits_list
    
'''
Runtime 97ms - Beats 31.43%
Memory 22.83MB - Beats 96.82%
'''