from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # defaultdict 생성, 기본값으로 빈 리스트 사용
        graph = defaultdict(list)

        # equations와 values를 zip으로 묶어 그래프 구성
        for (x, y), value in zip(equations, values):
            graph[x].append((y, value)) # x -> y 가중치
            graph[y].append((x, 1/value)) # y -> x 가중치(역수)

        def bfs(source, destination):
            # source에서 destination까지 가는 경로가 없는 경우
            if source not in graph or destination not in graph:
                return -1.0
            queue = deque([(source, 1.0)]) # (현재 노드, source에서 현재까지의 누적 가중치)
            visited = set() # 방문 기록 추적

            while queue:
                # 현재 노드와 현재 노드까지의 누적 가중치 할당
                current, current_weight = queue.popleft()
                # 현재 노드가 목적노드이면 현재 노드까지의 누적 가중치 반환
                if current == destination:
                    return current_weight
                # 방문 처리
                visited.add(current)
                # graph에서 현재 노드와 연결된 노드들 순회
                for connected, value in graph[current]:
                    # 연결되지 않았다면
                    if connected not in visited:
                        # 큐에 해당 노드와 현재까지의 누적 가중치에 value 곱해서 추가
                        queue.append((connected, current_weight * value))

            return -1.0
            
        # 각 쿼리에 대해 bfs 적용하여 결과 반환
        return [bfs(source, destination) for source, destination in queries]
    '''
    Runtime 35 ms - Beats 68.16%
    Memory 16.63 MB - Beats 53.75%
    '''