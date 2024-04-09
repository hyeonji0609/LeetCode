from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # 인덱스 기준    상    하      좌     우
        direction = [[-1,0],[1,0],[0,-1],[0,1]] # d[0] : 세로 d[1] : 가로
        que = deque() # queue 초기화
        que.append(entrance) # 큐에 처음 좌표 집어넣기 큐 에도 [y,x] 큐에는 리스트로
        
        visited = set() # visited 초기화
        visited.add((entrance[0],entrance[1])) # 방문처리 할 좌표 리스트 (y,x)
        
        width = len(maze[0])-1 # 인덱스 길이
        height = len(maze)-1 # 인덱스 높이
        
        step = 0 # 추적 steps
        while que: #큐가 살아 있다면
            step +=1 # 첫 발자국을 일단 떼고 
            for q in range(len(que)): # que길이 만큼 돌건데
                y,x = que.popleft() # que에서 첫번째거 팝 해서 y,x할당

                for d in direction: # direction을 돌자
                    ny = y+d[0] # 세로 이동한 좌표              
                    nx = x+d[1] # 가로 이동한 좌표
                    if (
                        0 <= nx <= width and # 이동한 x가 0이상 길이 이하 "이고"
                        0 <= ny <= height and # 이동한 y가 0이상 길이 이하 "이고"
                        maze[ny][nx] == "." and # 이동한 좌표가 "." "이고"
                        ((ny,nx) not in visited) # 방문하지 않았다면
                    ):
                        # 근데 이동 했을 때
                        # maginal한 자리라면
                        if ny == 0 or ny == height or nx == 0 or nx == width:
                            return step # 당장 step 반환
                        # 그 외 자리라면 계속 돌아야하므로
                        else: 
                            # que에 넣어주고 방문처리
                            que.append([ny,nx])
                            visited.add((ny,nx))
                        
        # 큐를 모두 다 돌았는데도 답이 없다면 -1처리
        return -1
    
"""
runtime : 688 ms / beats : 36.91%
memory : 18.18 / beats : 39.99%
"""

# set은 변하지 않는 값이기 때문에 튜플로 밖에 넣을 수 없음                        
# set_instance = set() # 1. 먼저 초기화 후
# set_instance.add((instance[0],instance[1])) # 2. set은 .add로 넣어주기 append