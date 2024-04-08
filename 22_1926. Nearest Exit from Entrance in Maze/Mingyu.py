from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 행 길이는 m, 열 길이는 n
        m, n = len(maze), len(maze[0])
        # 상(0,1), 하(0,-1), 좌(-1,0), 우(1,0)
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        # 초기 시작점은 entrance, number of steps=0
        queue = deque([(entrance[0], entrance[1], 0)])
        # 방문 추적
        visited = set((entrance[0], entrance[1]))

        while queue:
            x, y, steps = queue.popleft() # 위치와 누적 step 할당
            # x, y의 위치(인덱스)가 행, 열의 끝에 도달하고, 그 위치가 입구가 아닌 경우(즉, 출구)
            if (x == 0 or x == m-1 or y == 0 or y == n-1) and (x,y) != (entrance[0], entrance[1]):
                return steps # 현재까지의 스텝 반환
            
            # 입구에서 위치 이동
            for move_x, move_y in directions:
                new_x, new_y = x + move_x, y + move_y # 위치 이동
                # 이동한 위치가 maze 크기 안에 있고, 비어있으며, 방문하지 않은 경우
                if 0 <= new_x < m and 0 <= new_y < n and maze[new_x][new_y] == '.' and (new_x, new_y) not in visited:
                    # 방문 처리
                    visited.add((new_x, new_y))
                    # 이동한 위치와 steps + 1 큐에 추가
                    queue.append((new_x, new_y, steps + 1))
        # 출구 없으면 -1
        return -1
    '''
    Runtime 647 ms - Beats 78.05%
    Memory 18.16 MB - Beats 40.21%
    '''