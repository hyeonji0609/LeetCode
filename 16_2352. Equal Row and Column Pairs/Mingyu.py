class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # 행을 해시맵에 저장
        row_map = {}
        for i, row in enumerate(grid):
            key = tuple(row) # 각 행의 값 통째로 튜플로 변환해 key로 저장
            if key not in row_map:
                row_map[key] = 0
            row_map[key] += 1
        
        # 열을 row_map과 비교
        pair = 0
        # grid의 열 갯수만큼 순회
        for j in range(len(grid[0])):
            # 루프1 : 0,1,2번째 행의 0번 열
            # 루프2 : 0,1,2번째 행의 1번 열
            # 루프3 : 0,1,2번째 행의 2번 열
            col = tuple(grid[row][j] for row in range(len(grid)))
            # 각 열의 튜플이 row_map에 있는지 count
            if col in row_map:
                pair += row_map[col]
        
        return pair
    
    '''
    Runtime 397 ms - Beats 68.14%
    Memory 21.56 MB - Beats 58.29%
    '''