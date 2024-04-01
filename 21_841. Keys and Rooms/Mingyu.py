class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 방문 여부를 추적할 배열 rooms의 길이만큼 0으로 채워서 초기화
        visited = [0] * len(rooms)
        
        # 주어진 room i에서 시작하는 dfs 정의
        def dfs(i):
            # visited[i]를 1로 업데이트(방문 처리)
            visited[i] = 1
            # 현재 방 i에서 얻을 수 있는 모든 key를 순회
            for key in rooms[i]:
                # 방문하지 않은 방이 있으면
                if not visited[key]:
                    # 해당 방으로 이동
                    dfs(key)
        # 첫번째 방(0번)부터 순회 시작
        dfs(0)
        # visited가 전부 1(True)이면 True를 아니면 False를 return
        return all(visited)
    '''
    Runtime 66 ms - Beats 54.80%
    Memory 16.90 MB - Beats 93.76%
    '''