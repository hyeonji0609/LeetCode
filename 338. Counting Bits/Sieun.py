class Solution:
    def countBits(self, n: int) -> List[int]:
        count1_list = []
        for i in range(n+1):
            count1_list.append(bin(i).count('1'))
        return count1_list
    
"""
Runtime 77 ms
Memory 23.2 MB
"""