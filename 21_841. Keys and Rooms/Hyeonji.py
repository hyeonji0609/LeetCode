class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 방문한 노드를 담을 집합
        visited = set()

        def dfs(u):
            if u in visited:
                return

            # 방문한 노드가 아니면 add
            visited.add(u)

            # 현재 노드와 연결된 노드들을 dfs로 연결 
            for v in rooms[u]:
                dfs(v)
        
        dfs(0)

        return len(rooms) == len(visited)

"""
Runtime: 70 ms
Memory Usage: 17 MB
"""