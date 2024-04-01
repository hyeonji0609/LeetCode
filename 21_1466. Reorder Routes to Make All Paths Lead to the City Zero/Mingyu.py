from collections import defaultdict, deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # defaultdict 생성, 기본값으로 빈 리스트 사용
        graph = defaultdict(list)
        # connections를 순회하며, 연결된 city들을 추적
        for a, b in connections:
            # a에서 b로 가는 방향을 True로 설정(원래 연결되 방향)
            graph[a].append((b, True))
            # b에서 a로 가는 방향을 False로 설정(원래 연결의 역방향)
            graph[b].append((a, False))
        # 방문 여부를 처리할 배열을 n만큼 False로 채워서 초기화
        visited = [False] * n
        queue = deque([0])  # 0번 city에서부터 bfs를 수행할 queue 초기화
        change_count = 0 # 방향 변경 카운트 0으로 초기화

        while queue: # queue가 존재할 때까지 루프
            current = queue.popleft() # popleft로 현재 city 할당 
            visited[current] = True # 현재 city를 True로 업데이트(방문처리)

            for neighbor, direction in graph[current]: # current와 이웃한 모든 city를 순회
                if not visited[neighbor]: # 연결된 city를 방문 하지 않은 경우
                    queue.append(neighbor) # queue에 해당 city를 추가
                    # 0번 city로 가는 방향이 아니면, 방향 업데이트 필요
                    if direction:  # 즉, a에서 b로 가는 원래의 방향인 경우엔 업데이트해야 하므로 카운트 증가
                        change_count += 1
        
        return change_count

'''
Runtime 916 ms - Beats 71.36%
Memory 46.06 MB - Beata 65.72%
'''