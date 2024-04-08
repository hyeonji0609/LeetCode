from collections import deque

# 전략 : 1의 개수를 다 세고 빼 가면서 0으로 만들 수 있으면 cnt를 반환

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 인덱스 기준    상    하      좌     우
        direction = [[-1,0],[1,0],[0,-1],[0,1]]
        

        que = deque() # 큐 초기화
        one_num = 0 # 총 1의 개수 == fresh orange 
        height = len(grid) # 세로 길이
        width = len(grid[0]) # 가로 길이
        
        #### 2의 좌표와 1의 개수를 세는 반복문 ####        
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2: # 2라면 
                    que.append([j,i]) # [가로 좌표, 세로 좌표]
                elif grid[i][j] ==1:
                    one_num+=1
        #####################################
        if one_num == 0: # 1의 개수가 하나도 없으면 0리턴
            return 0
        
        time = 0
        while que:
            for q in range(len(que)): # 큐의 길이 만큼
                x,y = que.popleft() # xy좌표 받아오기
                
                for i in range(4):
                    if (
                        x + direction[i][1] < width and # 이동한 x 좌표가 가로 길이보다 작고
                        y + direction[i][0] < height and # 이동한 y좌표가 세로 길이보다 작고
                        x + direction[i][1] >=0 and # 이동한 x좌표가 0보다 크고
                        y + direction[i][0] >= 0 and # 이동한 y좌표가 0보다 크고
                        grid[y+direction[i][0]][x+direction[i][1]] ==1 # 이동한 grid[y][x]가 1일때
                    ): 
                        grid[y+direction[i][0]][x+direction[i][1]] = 2 # 이동한 좌표를 2로 바꿔주고
                        que.append([x+direction[i][1],y+direction[i][0]]) # 이동한 좌표를 que에 담기
                        one_num -= 1 # 한 좌표를 이동했으면 1의 총개수에서 빼주기
            time +=1 # 한 큐가 모두 끝나면 time을 1 추가

        return time-1 if one_num == 0 else -1

'''
runtime : 56ms / beats : 24.25%
memory : 16.75mb / beats : 8.82%
'''
                    
# 길이는 인덱스보다 하나 많은 것에 주의
# que의 길이 만큼 돌 때, 그 큐를 다 해소하고 나서야 time +1에 주의
# 그냥 인덱스랑 좌표랑 헷갈림에 주의
# bfs를 다룰 때는 2stage로 접근하자