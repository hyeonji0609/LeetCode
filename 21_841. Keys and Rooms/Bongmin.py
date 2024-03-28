class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # 비교할 rooms_nums를 만든다 1번째 예시로 들면 [0,1,2,3]이 만들어짐
        rooms_nums = [x for x in range(len(rooms))]
        
        def dfs_recursive(graph, node): 
            res = [] 
            visited = set() 

            def _dfs(u):
                if u in visited:
                    return
                visited.add(u) 
                res.append(u) 
                for v in graph[u]: 
                    _dfs(v) 

            _dfs(node) 
            return res
        # 모든 방을 다 돌 수 있다면 rooms_nums와 같다는 뜻이므로
        # rooms_nums의 노드를 반복문을 돌려서 재귀를 수행하게 한다.
        for i in rooms_nums:
            if sorted(dfs_recursive(rooms,i)) == rooms_nums:
                return True
            else:
                return False
        
"""
runtime : 72ms / beats : 19.87% - sorted랑 반복문을 돌려서 그런 듯 하다.
memory : 17.17mb / beats : 23.9% - rooms_nums를 할당해서?
"""