from collections import defaultdict, deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        # 상(0,1), 하(0,-1), 좌(-1,0), 우(1,0)
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        row, col = len(grid), len(grid[0])
        
        # 방문 node 저장
        visited = set()
        
        start = []

        for i in range(N):
            if 2 in grid[i]:
                start = [i, grid[i].index(2)]

        # 오렌지 갯수 세기
        orange = 0
        for i in range(N):
            orange += grid[i].count(1) + grid[i].count(2)
        
        # bfs
        def bfs(grid, start, visited):
            # 시작 노드 삽입
            queue = deque([(start[0], start[1], 0)])

            # 시작 노드 방문처리
            visited.add((start[0], start[1]))

            max_distance = 0

            while queue:
                x, y, distance = queue.popleft()

                # 최대 거리 갱신
                max_distance = max(max_distance, distance)

                # 갈 수 있는 방향은 4가지
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    if 0 <= new_x < row and 0 <= new_y < col and grid[new_x][new_y] == 1:
                        # 한번도 방문해보지 않았다면
                        if (new_x, new_y) not in visited:
                            visited.add((new_x, new_y))
                            queue.append((new_x, new_y, distance + 1))

            return max_distance, visited
        
        if not start:
            return 0 if orange == 0 else -1
        
        max_distance, visit = bfs(grid, start, visited)
        
        return max_distance if len(visit) == orange else -1

"""
False
"""