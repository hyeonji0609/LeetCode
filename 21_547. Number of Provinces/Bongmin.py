class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        isDict = {node : [] for node in range(len(isConnected))}
        # isConnected = [[1,1,0],[1,1,0],[0,0,1]]을
        # isDict = {0:[1],1:[0],2:[]}로 바꿔주는 과정
        for i in range(len(isConnected)):
            # i는 인덱스
            cnt = 0
            j_idx = 0
            for j in isConnected[i]:
                if i == cnt:
                    j_idx +=1
                else:
                    if j == 1:
                        isDict[i].append(j_idx)
                    j_idx+=1
                cnt+=1 
        ###############재귀##############
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
            return sorted(res) # sorted로 정렬시키기
        ###############재귀##############

        # 반복문을 돌려 모든 노드에서 그래프 순회
        ls = []
        for i in range(len(isDict)):
            ls.append(dfs_recursive(isDict,i))
        
        # 반복을 제거
        result = []
        for i in ls:
            if i not in result:
                result.append(i)
        return len(result)
'''
Runtime : 324ms / beats : 5%
Memory : 18.38mb / beats 7%
??
'''