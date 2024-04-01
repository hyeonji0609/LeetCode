class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # 방문여부를 추적할 배열을 city 개수 만큼 0(방문 x)으로 초기화
        visited = [0] * len(isConnected)
        # 연결된 갯수 count를 0으로 초기화
        count = 0
        # 주어진 city i에서 시작하는 dfs 정의
        def dfs(i):
            # i랑 연결된 모든 city j를 순회
            for j in range(len(isConnected)):
                # i와 j가 연결되어 있고, j를 아직 방문하지 않은 경우
                if isConnected[i][j] == 1 and not visited[j]:
                    # visited[j]를 1로 업데이트(방문 처리)
                    visited[j] = 1
                    # city j에서부터 다시 dfs 진행
                    dfs(j)

        # 전체 city를 순회
        for i in range(len(isConnected)):
            # 아직 방문하지 않은 city에서 dfs 시작
            if not visited[i]:
                # i에서부터 dfs 순회
                dfs(i)
                # count 1씩 증가
                count += 1
                
        return count
    '''
    Runtime 176 ms - Beats 90.30%
    Memory 17.75 MB - Beats 16.70%
    '''