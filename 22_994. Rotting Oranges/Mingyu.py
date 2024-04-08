from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 행 길이는 m, 열 길이는 n
        m , n = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0 # 신선한 오렌지 수
        time = 0 # 초기 시간

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2: # 썩은 오렌지이면,
                    queue.append((row, col, time)) # 큐에 행,열과 초기 시간 추가

                elif grid[row][col] == 1: # 신선한 오렌지면,
                    fresh_oranges += 1 # 갯수 세기

        # 상(0,1), 하(0,-1), 좌(-1,0), 우(1,0)
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        time_flow = 0 # 흐른 시간
        while queue:
            row, col, time = queue.popleft() # 큐에서 썩은 오렌지 위치와 초기 시간 꺼내 할당
            time_flow = max(time_flow, time) # 흐른 시간 업데이트

            for move_row, move_col in directions: # 썩은 오렌지 위치에서 이동
                new_row, new_col = row + move_row, col + move_col # 이동한 위치 반영

                # 이동한 위치가 grid 범위 안에 있고, 신선한 오렌지이면
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2 # 썩은 오렌지로 업데이트
                    fresh_oranges -= 1 # 신선한 오렌지 갯수 줄이기
                    queue.append((new_row, new_col, time + 1)) # 큐에 썩은 오렌지 위치와 시간+1 해서 추가

        # 모든 오렌지가 썩었으면 그 시간을 반환 그렇지 않으면 -1을 반환
        return time_flow if fresh_oranges == 0 else -1
    '''
    Runtime 54 ms - Beats 35.42%
    Memory 16.53 MB Beats 66.11%
    '''