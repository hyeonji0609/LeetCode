from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 상(0,1), 하(0,-1), 좌(-1,0), 우(1,0)
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        row, col = len(maze), len(maze[0])
        
        # 방문 node 저장
        visited = set()
        
        def bfs(maze, entrance, visited):
            # 시작 노드 삽입
            queue = deque([(entrance[0], entrance[1], 0)])

            # 시작 노드 방문처리
            visited.add((entrance[0], entrance[1]))

            while queue:
                # 큐에서 노드를 꺼냄
                x, y, distance = queue.popleft()

                if (x == 0 or x == row-1 or y == 0 or y == col-1) and (x, y) != (entrance[0], entrance[1]):
                    return distance

                # 갈 수 있는 방향은 4가지
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy

                    if (0 <= new_x < row) and (0 <= new_y < col):
                        if maze[new_x][new_y] == ".":
                            # 한번도 방문해보지 않았고, 통로이면
                            if (new_x, new_y) not in visited :
                                visited.add((new_x, new_y))
                                queue.append((new_x, new_y, distance+1))

            return -1
        
        return bfs(maze, entrance, visited)

"""
Runtime: 664 ms
Memory Usage: 18.2 MB
"""