class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashtable = {}
        count = 0
        
        for row in grid:
            # 각각의 row를 key로 만들어 줌
            try: 
                hashtable[tuple(row)] += 1 # 만약 딕셔너리에 키가 있으면 value 값 +1 
            except:
                hashtable[tuple(row)] = 1 # 키가 없으면 value 값 1로 초기화
 
        # column 기준의 grid를 새로 만들어 줌
        perpendicular = [(i) for i in list(zip(*grid))[:]]
        
        for row in perpendicular: 
            if row in hashtable: # 만약 column 값이 hashtable 안에 있으면
                count += hashtable[row] # value값을 count에 더해줌
        
        return count

"""
Runtime: 357 ms
Memory Usage: 21.5 MB
"""
        