class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = {}
        
        for idx, row in enumerate(mat) :
            count[idx] = row.count(1) # key : 인덱스, value : 1의 갯수
            
        sorted_count = sorted(count.items(), key=lambda item: item[1]) # dict를 value 기준으로 정렬
        
        return [row[1][0] for row in enumerate(sorted_count[:k])] # k번째 인자까지 return

"""
Runtime: 90 ms
Memory Usage: 16.9 MB
"""