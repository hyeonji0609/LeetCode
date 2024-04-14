class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path):
            nonlocal paths # paths는 dfs안에서 정의된 함수가 아님

            if not node:
                return
            # 지금까지의 경로에 현재 노드를 남아주기
            path.append(str(node.val)) # join은 str만 취급. int따위는 취급하지 않음. 
            # node에서 왼쪽 오른쪽 모두 없다면 leaf이므로
            if not node.left and not node.right:
                # 지금까지의 경로를 모두 -> join해서 paths(결과)에 담ㅇ주기
                paths.append("->".join(path))
                
            else:
                # 재귀
                dfs(node.left, path)
                dfs(node.right, path)
            # 백트래킹으로 이전 상태로 돌아가기 
            path.pop()
            
        # root가 없는 경우
        if not root:
            return []
        
        paths = []
        dfs(root, [])
        return paths

'''
runtime : 35ms / beats : 71.59%
memory : 16.6mb / beats : 47.15%
'''