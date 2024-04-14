from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # 상(0,1), 하(0,-1), 좌(-1,0), 우(1,0)
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        row, col = len(grid), len(grid[0])
        
        # 방문 node 저장
        visited = set()
        queue = deque()

        # 오렌지 갯수 세기
        orange = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    orange += 1
                elif grid[r][c] == 2:
                    queue.append([r, c, 0])
        
        # bfs
        max_minutes = 0
        
        while queue:
            x, y, minutes = queue.popleft()

            # 최대 거리 갱신
            max_minutes = max(max_minutes, minutes)

            # 갈 수 있는 방향은 4가지
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                # 좌표가 grid안에 있고, 신선한 오렌지이며, 방문하지 않았다면
                if 0 <= new_x < row and 0 <= new_y < col:
                    if grid[new_x][new_y] == 1 :
                        # 신선한 오렌지 -> 썩은 오렌지로
                        grid[new_x][new_y] = 2
                        orange -= 1

                        # 방문 처리
                        queue.append((new_x, new_y, minutes + 1))

        return max_minutes if orange == 0 else -1          
        
"""
Runtime: 50 ms
Memory Usage: 16.6 MB
"""